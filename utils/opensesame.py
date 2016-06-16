import os
from AppKit import NSAlert, NSAlertSecondButtonReturn, NSAlertFirstButtonReturn, NSAlertThirdButtonReturn
from vanilla.dialogs import getFile, getFileOrFolder, putFile
from robofab.world import CurrentFont, AllFonts, OpenFont

class OpenSesame:
    
    @classmethod
    def collectFiles(cls, srcs=[], ext=['.ufo']):
        """
        Walk through all subfolders of the given path and return files with a certain extension.
        """
        if not srcs:
            src = getFileOrFolder('Where are the UFOs?', allowsMultipleSelection=False)[0]
        print src

        paths = []
        for root, dirs, files in os.walk(src):
            for directory in dirs:
                basePath, extension = os.path.splitext(directory)
                if extension in ext:
                    paths.append(os.path.join(root, directory))
        return paths
    
    @classmethod
    def getFont(cls, f, showUI=False):
        """
        Given a font or the path of a font, return the font.
        """
        if f is None:
            return f
        try:
            if f.path:
                pass
            return f
        except:
            for potentialFont in AllFonts():
                if potentialFont.path is not None and potentialFont.path == f:
                    return potentialFont
        return OpenFont(f, showUI=showUI)
    
    @classmethod
    def getPath(cls, f):
        """
        Given a font or the path of a font, return the path.
        """
        try:
            return f.path
        except:
            return f
    
    @classmethod
    def saveIfUnopened(cls, f):
        """
        If the file isn't open, we have to change it for changes to take effect.
        """
        try:
            if f.document() is None:
                f.save()
        except:
            pass

    @classmethod
    def collect(cls, returnMethod=False):
        buttonTitlesValues = [
            ('All Open', 0), 
            ('Current', 1), 
            ('Selection', 2), 
            ('Cancel', 4)
            ]
        """
        A dinky little interface for batch processing.
        """
        messageText = 'Select fonts from...'
        result = []
        method = None
        alert = NSAlert.alloc().init()
        alert.setMessageText_(messageText)
        for buttonTitle, value in buttonTitlesValues:
            alert.addButtonWithTitle_(buttonTitle)
        code = alert.runModal()
        if code == NSAlertFirstButtonReturn:
            result = AllFonts()
            method = 'AllFonts'
        elif code == NSAlertSecondButtonReturn:
            f = CurrentFont()
            if f is not None:
                result = [CurrentFont()]
            else:
                result = []
            method = 'CurrentFont'
        elif code == NSAlertThirdButtonReturn:
            method = 'Selection'
            result = cls.collectFiles(ext=['.ufo'])
        if returnMethod:
            return (result, method)
        else:
            return result
            
if __name__ == "__main__":
    # return a list of either fonts or paths
    for fop in OpenSesame.collect():
        f = OpenSesame.getFont(fop, showUI=False)
        print 'Working on %s...' %OpenSesame.getPath(fop)
        for g in f:
            print '\tDo something to', g       
        #OpenSesame.saveIfUnopened(fop)
        f.close()
    print 'done'