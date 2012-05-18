# encoding: utf-8
#===============================================================================
# Tareas rutinarias
# Compilar los $(NAME).UI en ui_$(NAME).py
# Crear exe? 
#===============================================================================
from fabric.api import *

UI_DIRECTORY = 'resources/ui'
UI_TARGET_DIR = 'gui/ui'
PYRCC = '/usr/bin/pyuic'

from os import path

def _iter_ui_py_rules(top_dir, dest_callback):
    '''
    @param top_dirparam: Directorio por donde empezar a cazar uis
    @param dest_callback: Función que transforma una ruta a ui a su destino
    '''
    import fnmatch, os
    for basepath, _subdirs, filenames in os.walk(top_dir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, "*.ui"):
                # Es una UI
                filepath = path.join(basepath, filename) 
                relative_path = path.relpath(basepath, top_dir)
                yield (filepath, dest_callback(relative_path, filename))

def _is_older_file(source, dest):
    '''True si dest es más viejo que source'''
    if not path.exists(dest):
        return True
    from os.path import getmtime
    return getmtime(source) > getmtime(dest)

def _check_path_is_package(dirpath):
    ''' Para que un directorio dirpath sea una paquete en python
    tiene que contener el archivo __init__.py, esta función
    checkea que cada subdirectorio del path sea contenga 
    su __init__.py, creándolo si es necesario'''
    assert path.isdir(dirpath)
    dirs = filter(bool, dirpath.split(path.sep))
    for n in range(len(dirs)):
        target = path.join(dirs[:n] + ['__init__.py'])
        if not path.exists(target):
            with open(target, 'w') as f:
                pass
        
    
def _compile_ui(source, dest):
    ''' Compila un .ui en un .py si esta desactualizado'''
    import os
    destdir = path.dirname(dest)
    if not path.exists(destdir):
        os.makedirs(destdir)
    _check_path_is_package(destdir)
    local('{PYRCC} {SOURCE} -o {DEST}'.format(
                                               SOURCE = source,
                                               DEST = dest,
                                               PYRCC = PYRCC
                                               ))
    
def ui():
    """Compile resources"""
    from os.path import splitext, join, abspath, dirname
    def dest_callback(basepath, filename):
        barename, _ = splitext(filename) # aaa.bb -> barename = aaa, _ = bb 
        filename = "ui_%s.py" % barename
        return abspath(join(UI_TARGET_DIR, basepath, filename))
    
    for source, dest in _iter_ui_py_rules(UI_DIRECTORY, dest_callback):
        if _is_older_file(source, dest):
            _compile_ui(source, dest)
        