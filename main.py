#!/bin/env python

import argparse
import os
import sys

import scanner
import handler

def main():
    handlers = handler.Handlers()
    handlers.add_handler(handler.PrintHandler())

    parser = argparse.ArgumentParser(description='Scan and alter music directories.')
    parser.add_argument('basedir', help='The directory to work on')
    args = parser.parse_args()

    basedir=os.path.abspath(args.basedir)
    musicdirs=scanner.scan_dir(basedir)

    for m in musicdirs:
        if m.contains_music():
            handlers.handleDirectoryWithMusicFiles(m)
        elif not m.contains_dirs():
            if m.contains_files():
                handlers.handleDirectoryWithoutMusicFiles(m)
            else:
                handlers.handleEmptyDirectory(m)

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)

