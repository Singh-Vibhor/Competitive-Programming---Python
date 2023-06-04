import magic
import gzip
import tarfile
import os
import shutil



def checkfiletype(filename):
    return magic.from_file(filename, mime=True)


def gzipopen(filename):
    with open(filename, 'rb') as f:
        a = f.read()
        gzip.decompress(a)
        with open(filename, 'wb') as f:
            f.write(a)

def taropen(filename):
    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()



filename = './f1/archive'
x = 0
print(checkfiletype(filename))
while True:
    print(checkfiletype(filename=filename),x)

    if checkfiletype(filename=filename).endswith('gzip'):
        if x%2:    
            gzipopen(filename = filename)

        else:
            taropen(filename=filename)
        

    else:
        break