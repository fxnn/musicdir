#!/bin/env python

import os

known_music_extensions={'mp3', 'flac', 'ogg', 'wav', 'wma', '3gp', 'aac', 'aiff', 'au', 'dss', 'm4a', 'oga', 'opus', 'webm'}

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

