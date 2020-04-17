#!/bin/env python

import sys
import os

known_music_extensions={'mp3', 'flac', 'ogg', 'wav', 'wma', '3gp', 'aac', 'aiff', 'au', 'dss', 'm4a', 'oga', 'opus', 'webm'}
ignored_dir_names={'@eaDir'}

def main():
    basedir=sys.argv[1]
    if not basedir:
        print "usage: %s basedir" % sys.argv[0]
        return 1
    basedir=os.path.abspath(basedir)
    musicdirs=scan_dir(basedir)
    for musicdir in musicdirs:
        if not musicdir.contains_music() and not musicdir.contains_dirs():
            if musicdir.contains_files():
                print('no music: %s' % musicdir.abspath)
            else:
                print('empty: %s' % musicdir.abspath)
    return 0

class MusicDir:
    def __init__(self, abspath):
        self.abspath=abspath
        self.dirs=set()
        self.files=set()
        self.extensions=set()
    def add_file(self, filename):
        self.files.add(filename)
        extension=os.path.splitext(filename)[1]
        if extension:
            self.extensions.add(extension[1:].lower())
    def add_dir(self, dirname):
        self.dirs.add(dirname)
    def contains_files(self):
        return len(self.files)>0
    def contains_music(self):
        return len(known_music_extensions.intersection(self.extensions))>0
    def contains_dirs(self):
        return len(self.dirs)>0

def scan_dir(basedir):
    musicdirs=[]
    for root, subdirs, files in os.walk(basedir):
        if not is_ignored_path(root):
            musicdir=MusicDir(root)
            musicdirs.append(musicdir)
            for file in files:
                musicdir.add_file(file)
            for subdir in subdirs:
                if not subdir in ignored_dir_names:
                    musicdir.add_dir(subdir)
    return musicdirs

def is_ignored_path(path):
    normpath = os.path.normpath(path)
    normpath_split = normpath.split(os.sep)
    return len(ignored_dir_names.intersection(normpath_split)) > 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)

