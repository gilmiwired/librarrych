import time
import os
import sys
import datetime
import subprocess
from multiprocessing import Process

def run_proc():
    subprocess.call(["fswebcam","{}.jpg".format(b),"-q"])

def daemonize():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc)
    print('start child process.')
    p.start()
    p.join()
    print('end child process.')
    subprocess.call(["rm","-f","top.jpg"])
    subprocess.call(["cp","-s","{}.jpg".format(b),"top.jpg"])
    subprocess.call(["bash","commit.sh"])
    subprocess.call(["rm","-f","{}.jpg".format(b-2)])
    subprocess.call(["bash","commit.sh"])


b = 1

if __name__ == '__main__':
    while True:
        daemonize()
        b += 1
        time.sleep(60)
