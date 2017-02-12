import os

def main(cmd):
    print "Command list:"
    for comd in os.listdir('us'):
        if os.path.isfile('us/'+comd):
            print comd[:-3].upper()
    for comd in os.listdir('network'):
        if os.path.isfile('us/'+comd) and comd.endswith('.py'):
            print comd[:-3].upper()

if __name__ == '__main__':
    os.chdir('..')
    main()
