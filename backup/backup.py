import time
import os
import sys
import datetime
import subprocess
from multiprocessing import Process

def run_proc():
    subprocess.call(["fswebcam","{}.jpg".format(num),"-q"])

def daemonize():
    p = Process(target=run_proc)
    p.start()
    p.join()

num = 1

if __name__ == '__main__':
    while True:
        daemonize()
        if num == 100:
          num = 1
        num += 1
        time.sleep(60)
