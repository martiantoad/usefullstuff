import os

global cus

print "UsefullStuff command line"
cus = "user"

def setCus(ncus):
    cus = ncus

def getCus():
    return cus

def getCommand():
    command = raw_input("US://%s" % cus + ': ')
    return command

def procCommand(command):
    for pyfile in os.listdir('us'):
        if os.path.isfile('us/'+pyfile):
            if pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'us.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                return 0
    for pyfile in os.listdir('network'):
        if os.path.isfile('network/'+pyfile):
            if pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'network.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                return 0
    for pyfile in os.listdir('math'):
        if os.path.isfile('math/'+pyfile):
            if pyfile[:-3] == command[:(len(pyfile[:-3]))]:
                pymod = 'math.' + pyfile[:-3]
                pyf = __import__(pymod, fromlist=[''])
                pyf.main(command[(len(pyfile[:-2])):])
                return 0
    return 1

while True:
    procCommand(getCommand())
