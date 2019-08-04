# Open Sesame

A quick RoboFont utility to give you a dialog that lets you choose if you want to run your script on:

* A selection of font files
* The current font
* All open fonts

![preview.png](preview.png)

## Using it

```
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
```