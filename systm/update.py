import wget
import os
import zipfile
import shutil

def main():
    wget.download("https://github.com/handsomebelugawhale/usefullstuff/releases/download/1.0.0-beta.2/update-usefullstuff-1.0.0-beta.2.zip")
    updatezip = zipfile.ZipFile('update-usefullstuff-1.0.0-beta.2.zip')
    os.rename('network', 'network_old')
    os.rename('umath', 'umath_old')
    os.rename('us', 'us_old')
    os.rename('readme.md', 'readme.md_old')
    os.rename('LICENSE.md', 'LICENSE.md_old')
    os.rename('setup.py', 'setup.py_old')
    updatezip.extractall()
    updatezip.close()
    shutil.rmtree('network_old')
    shutil.rmtree('umath_old')
    shutil.rmtree('us_old')
    os.remove('readme.md_old')
    os.remove('setup.py_old')
    os.remove('update-usefullstuff-1.0.0-beta.2.zip')
