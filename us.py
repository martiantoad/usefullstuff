import os
import umath.settings
import network.settings
import us.settings

print "UsefullStuff command line"

def setCus(ncus):
    global cus
    cus = ncus
    umath.settings.cus = ncus
    network.settings.cus = ncus
    us.settings.cus = ncus

setCus("user")

def getCus():
    return cus

def getCommand():
    command = raw_input("US://%s" % cus + ': ')
    return command

def procCommand(command):
    if command == 'cm update':
        import systm.update
        systm.update.main()
    if command[:2] == 'cd':
        setCus(command[3:])
        return 0
    if command[:8] != 'settings':
        for pyfile in os.listdir('us'):
            if os.path.isfile('us/'+pyfile) and pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'us.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                return 0
        for pyfile in os.listdir('network'):
            if os.path.isfile('network/'+pyfile) and pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'network.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                return 0
        for pyfile in os.listdir('umath'):
            if os.path.isfile('umath/'+pyfile) and pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'umath.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                return 0
    return 1

while True:
    procCommand(getCommand())
