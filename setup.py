import sys

if sys.version_info<(2,7,12) or sys.version_info>=(3,0):
    sys.exit('Python version must 2.7.12 or above, and also not 3')

import os
import urllib2
try:
    import pip
except Exception:
    getpipurl = urllib2.urlopen('https://bootstrap.pypa.io/get-pip.py')
    getpip = __import__(getpipurl, fromlist=[''])
    getpip.main()

def install(pkg):
    pip.main(['install', pkg])

def main():
    install('wget')
    install('netaddr')

if __name__ == '__main__':
    if sys.version_info<(2,7,12) or sys.version_info>=(3,0):
        sys.exit('Python version must 2.7.12 or above, and also not 3')
    else:
        main()
