from utils.opensesame import OpenSesame
# return a list of either fonts or paths
for fop in OpenSesame.collect():
    f = OpenSesame.getFont(fop, showUI=False)
    print 'Working on %s...' %OpenSesame.getPath(fop)
    for g in f:
        print '\tDo something to', g       
    #OpenSesame.saveIfUnopened(fop)
    f.close()
print 'done'