import os

def main(cmd):
    if cmd == "scripts":
        pass
    else:
        print "exit - This command exits the command line"
        print "cd <directory> - This changes your directory"
        print "mkdir <directory> - This makes a directory"
        print "rmdir <directory> - This deletes a directory"
        print "mk <filename> - This makes a file"
        print "rm <filename> - This deletes a file"
        print "dir - This prints your current directory"
        print "log print - This prints the log"
        print "<script> <*args> - This runs a script"
