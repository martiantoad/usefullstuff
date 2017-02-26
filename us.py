import os
import sys
import shutil
from systm.exception import unknown_exception as error
import umath.settings
import network.settings
import us.settings
import systm.log as log
import wget

log.add("imported core modules")

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
    if command == 'exit':
        sys.exit()
    if command == 'cm update':
        os.chdir('systm')
        os.rename('update.py', 'update.py_old')
        wget.download('https://raw.githubusercontent.com/handsomebelugawhale/usefullstuff/master/systm/update.py')
        os.remove('update.py_old')
        import systm.update
        systm.update.main()
        log.add("updated")
        return 0
    if command[:2] == 'cd':
        #Change this after adding user system
    	if command == 'cd ..' and len(cus) > 4:
            setCus(cus.rsplit('/', 1)[0])
            log.add("directory changed")
    	    return 0
    	elif os.path.isdir(cus + '/' + command[3:]):
    	    setCus(cus + '/' + command[3:])
    	    log.add("directory changed")
    	    return 0
        else:
            print "Directory unchanged"
            log.add("directory not changed")
            return 0
    if command[:6] == 'mkdir ':
        os.makedirs(cus + '/' + command[6:])
        log.add('made directory %s' % command[6:])
        return 0
    if command[:3] == 'mk ':
        open(cus + "/" + command[3:], 'w')
        log.add('made file %s' % command[3:])
        return 0
    if command[:3] == 'rm ':
        os.remove(cus + "/" + command[3:])
        log.add('deleted %s' % command[3:])
        return 0
    if command[:6] == 'rmdir ':
        shutil.rmtree(cus + "/" + command[6:])
        log.add('deleted %s' % command[6:])
        return 0
    if command == 'dir':
        print cus
        log.add('printed cus')
        return 0
    if command == 'log print':
        log.print_log()
        log.add("log printed")
        return 0
    if command[:8] != 'settings':
        for pyfile in os.listdir('us'):
            if os.path.isfile('us/'+pyfile) and pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'us.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                log.add(pymod + " executed")
                return 0
        for pyfile in os.listdir('network'):
            if os.path.isfile('network/'+pyfile) and pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'network.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                log.add(pymod + " executed")
                return 0
        for pyfile in os.listdir('umath'):
            if os.path.isfile('umath/'+pyfile) and pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'umath.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                log.add(pymod + " executed")
                return 0
    print "Command/Script not found"
    log.add("command/script %s was not found" % command)
    return 1

log.add("initialized")

#add login prompt when user system added

while True:
    try:
        current_command = getCommand()
        log.add("user enterd command " + current_command)
        procCommand(current_command)
    except Exception as ex:
        #log.add("some exception happend, running exception manager")
        #error(ex)
        print ex
