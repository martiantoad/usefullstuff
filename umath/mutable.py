import systm.log

def main(mode):
    if mode == "print":
        for st in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
            for nd in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
                aws = st*nd
                print ("{}*{}={}").format(st, nd, aws)
                systm.log.add("printed mult table (1-16)")
