#!/bin/env python

import argparse
import os
import sys

import scan

def main():
    parser = argparse.ArgumentParser(description='Scan and alter music directories.')
    parser.add_argument('basedir', help='The directory to work on')
    args = parser.parse_args()

    basedir=os.path.abspath(args.basedir)
    musicdirs=scan.scan_dir(basedir)

    for m in musicdirs:
        if not m.contains_music() and not m.contains_dirs():
            if m.contains_files():
                print('no music: %s' % m.abspath)
            else:
                print('empty: %s' % m.abspath)

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)

