#!/bin/env python

import os

import musicdir

ignored_dir_names={'@eaDir'}

def scan_dir(basedir):
    musicdirs=[]
    for root, subdirs, files in os.walk(basedir):
        if not is_ignored_path(root):
            m=musicdir.MusicDir(root)
            musicdirs.append(m)
            for f in files:
                m.add_file(f)
            for s in subdirs:
                if not s in ignored_dir_names:
                    m.add_dir(s)
    return musicdirs

def is_ignored_path(path):
    normpath = os.path.normpath(path)
    normpath_split = normpath.split(os.sep)
    return len(ignored_dir_names.intersection(normpath_split)) > 0

