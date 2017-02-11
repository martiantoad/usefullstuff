import wget
import os
import settings

def main(url):
    originaldir = os.getcwd()
    os.chdir(settings.cus)
    dlfile = wget.download(url)
    os.chdir(originaldir)
