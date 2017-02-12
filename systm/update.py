import wget
import os
import zipfile
import shutil

def main():
    wget.download("https://github.com/handsomebelugawhale/usefullstuff/archive/master.zip")
    updatezip = zipfile.ZipFile('usefullstuff-master.zip')
    os.rename('network', 'network_old')
    os.rename('umath', 'umath_old')
    os.rename('us', 'us_old')
    os.rename('options.html', 'options.html_old')
    os.rename('readme.md', 'readme.md_old')
    os.rename('setup.py', 'setup.py_old')
    updatezip.extractall()
    for zfile in updatezip.namelist():
        if zfile != 'usefullstuff-master/us.py' and 'usefullstuff-master/main.c' and not zfile.startswith('usefullstuff-master/systm') and os.path.isfile(zfile):
            shutil.move(zfile, zfile[20:])
    shutil.rmtree('network_old')
    shutil.rmtree('umath_old')
    shutil.rmtree('us_old')
    os.remove('options.html_old')
    os.remove('readme.md_old')
    os.remove('setup.py_old')
    shutil.rmtree('usefullstuff-master')
    os.remove('usefullstuff-master.zip')
