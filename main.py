#!/bin/env python

import argparse
import os
import sys

import scanner
import handler

class Application:
    args = {}

    def __init__(self):
        self.args = self.parse_args()

    def run(self):

        music_dirs = self.scan()
        handlers = self.create_handlers()

        self.apply_handlers(music_dirs, handlers)

        return 0

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Scan and alter music directories.')
        parser.add_argument('basedir', help='The directory to work on')
        parser.add_argument('-p', '--print', action='store_true')
        parser.add_argument('-v', '--verbose', action='store_true')
        return vars(parser.parse_args())

    def scan(self):
        basedir=os.path.abspath(self.args['basedir'])
        return scanner.scan_dir(basedir)

    def create_handlers(self):
        handlers = handler.Handlers()
        if self.args['print'] or self.args['verbose']:
            handlers.append(handler.PrintHandler())
            if self.args['verbose']:
                handlers.append(handler.VerbosePrintHandler())
        return handlers

    def apply_handlers(self, music_dirs, handlers):
        for m in music_dirs:
            if m.contains_music():
                handlers.handleDirectoryWithMusicFiles(m)
            elif not m.contains_dirs():
                if m.contains_files():
                    handlers.handleDirectoryWithoutMusicFiles(m)
                else:
                    handlers.handleEmptyDirectory(m)

if __name__ == '__main__':
    status = Application().run()
    sys.exit(status)

