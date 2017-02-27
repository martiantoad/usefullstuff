from math import *
import systm.log

def main(cmd):
    try:
        prod = eval(cmd)
        print prod
        systm.log.add("calculated %s" % cmd)
    except Exception:
        print "Error, unable to calculate"
        systm.log.add("unable to calculate %s" % cmd)
