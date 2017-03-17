import settings
import os
from systm import log

def main(cmd):
    cud = settings.cus
    if cmd[:7] == "python ":
        os.system("python " + settings.cus + "/" + cmd[7:])
        log.add("ran %s using python" % cmd[7:])
    elif cmd[:8] == "pythonw ":
        os.system("pythonw " + settings.cus + "/" + cmd[8:])
        log.add("ran %s using python no console" % cmd[8:])
    elif cmd[:5] == "ruby ":
        os.system("ruby " + settings.cus + "/" + cmd[5:])
        log.add("ran %s using ruby" % cmd[5:])
    elif cmd == "nope":
        print "nope"
#:3 = first three only

class CustomRun():
    def __init__(self, compiler_name):
        self.compiler = compiler_name
    def run(self, path):
        os.system(self.compiler + " " + path)
