import sys,os
import os.path as path
i=1
directory= str(sys.argv[1])
directory=path.realpath(directory)
if path.isdir(directory):
    os.chdir(directory)
    files=os.listdir(directory)
    for f in files:
        os.rename(f,f'{sys.argv[2]} ({i})')

        i+=1