from utils.opensesame import OpenSesame
# return a list of either fonts or paths
for fontOrPath in OpenSesame.collect():
    # get a font object
    f = OpenSesame.getFont(fontOrPath, showUI=False)
    # get a path object
    print('Working on %s...' %OpenSesame.getPath(fontOrPath))
    # work on glyphs
    for g in f:
        print('\tDo something to', g)
        # ...
        # put your code here!
        # ...
    # do you want to save the file only if it is unopened?
    # OpenSesame.saveIfUnopened(fop)
    f.close()
print('done')