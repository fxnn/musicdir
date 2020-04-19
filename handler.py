#!/usr/bin/env python

class Handler(object):
    def handleEmptyDirectory(self, musicDir):
        pass
    def handleDirectoryWithoutMusicFiles(self, musicDir):
        pass
    def handleDirectoryWithMusicFiles(self, musicDir):
        pass

class PrintHandler(Handler):
    def handleEmptyDirectory(self, musicDir):
        print("empty   : " + musicDir.get_abspath())
    def handleDirectoryWithoutMusicFiles(self, musicDir):
        print("no music: " + musicDir.get_abspath())

class VerbosePrintHandler(PrintHandler):
    def handleDirectoryWithMusicFiles(self, musicDir):
        print("music   : " + musicDir.get_abspath())

class Handlers(Handler):
    handlerList = []

    def add_handler(self, handler):
        self.handlerList.append(handler)

    def handleEmptyDirectory(self, musicDir):
        self._invokeHandler(musicDir, "handleEmptyDirectory")
    def handleDirectoryWithoutMusicFiles(self, musicDir):
        self._invokeHandler(musicDir, "handleDirectoryWithoutMusicFiles")
    def handleDirectoryWithMusicFiles(self, musicDir):
        self._invokeHandler(musicDir, "handleDirectoryWithMusicFiles")
    def _invokeHandler(self, musicDir, handlerName):
        for h in self.handlerList:
            getattr(h, handlerName)(musicDir)
    
