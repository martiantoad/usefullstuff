import os

def main():
    print "Command list:"
    for comd in os.listdir('us'):
        if os.path.isfile('us/'+comd):
            print comd[:-3].upper()
    for comd in os.listdir('network'):
        if os.path.isfile('us/'+comd):
            if comd.endswith('.py'):
                print comd[:-3].upper()

if __name__ == '__main__':
    os.chdir('..')
    main()
