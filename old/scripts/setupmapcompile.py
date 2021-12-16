import os
import sys.argv
import urllib.request

def download(file):
    loc = "./dontpush/" + file.split("/")[-1]
    if (not os.path.exists(loc)):
        urllib.request.urlretrieve(file, loc)
    else:
        print("File Already Exists: " + loc)

if not os.path.exists("./dontpush"):
    os.makedirs("./dontpush")
