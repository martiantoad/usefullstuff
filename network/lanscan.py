#Thanks opentechguides.com for helping with this

import os
import platform
import netaddr
import threading

def scaniprange((lipr)):
    for item in lipr:
        output = os.system(command, item)
        if "unreachable" or "offline" in output:
            print(str(item), "is Offline")
        elif "timed out" in output:
            print(str(item), "is probebly Offline")
        else:
            print(str(item), "is Online")

def main():
    ipmi = raw_input("Enter min ip: ")
    ipma = raw_input("Enter max ip: ")
    ah = list((netaddr.iter_iprange(ipmi, ipma)))
    if platform.system().lower() == 'windows':
        command = 'ping -n 1 -w 500 '
    elif platform.system().lower() == 'linux' or platform.system().lower == 'linux2':
        command = 'ping -c 1 -W 500'
    elif platform.system().lower() == 'mac':
        command = 'ping -c 1 -t 500 '
    else:
        print "OS not supported"
        return 0
    lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    llo = len(ah)/(len(ah)/4)
    ahs = lol(ah, llo)
    ia = 0
    lip = ahs[ia]
    for item in ahs:
        threading.Thread(target=scaniprange,args=(lip)).start()
        ia = ia+1

main()
