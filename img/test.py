import time
import os
import sys
import datetime
import subprocess
from multiprocessing import Process

def run_proc():
    subprocess.call(["fswebcam","top.jpg","-q"])
    subprocess.call(["bash","commit.sh"])

def daemonize():
    print('Parent process %s.' % os.getpid())
    subprocess.call(["rm","-r","top.jpg"])
    p = Process(target=run_proc)
    print('start child process.')
    p.start()
    p.join()
    print('end child process.')
    subprocess.call(["bash","commit.sh"])


b = 1

if __name__ == '__main__':
    while True:
        daemonize()
        b += 1
        time.sleep(60)
