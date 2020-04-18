#!/bin/env python

import sys
import os

import scan

def main():
    basedir=sys.argv[1]
    if not basedir:
        print "usage: %s basedir" % sys.argv[0]
        return 1
    basedir=os.path.abspath(basedir)
    musicdirs=scan.scan_dir(basedir)
    for musicdir in musicdirs:
        if not musicdir.contains_music() and not musicdir.contains_dirs():
            if musicdir.contains_files():
                print('no music: %s' % musicdir.abspath)
            else:
                print('empty: %s' % musicdir.abspath)
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)

