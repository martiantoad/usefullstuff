#Thanks opentechguides.com for helping with this

import os
import platform

def main(cmd):
    if platform.system().lower() == 'windows':
        command = 'ping -n 1 -w 500 '
    elif platform.system().lower() == 'linux' or platform.system().lower == 'linux2':
        command = 'ping -c 1 -W 500'
    elif platform.system().lower() == 'mac':
        command = 'ping -c 1 -t 500 '
    else:
        print "OS not supported"
        return "os not supported"
    if cmd != "":
        print "Range configuration is not avalable (yet)"
    st = "192.168."
    for nd in range(0, 255):
        cip = st + str(nd) + "." + str(nd)
        #this is still wip
        os.system(command+cip)
