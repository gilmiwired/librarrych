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
	if((b-n) < 200):
		for i in range(n,(b-100)):
			subprocess.call(["rm","-r","{}.jpg".format(i)])
		n += 100
b = 1
n = 1

if __name__ == '__main__':
    while True:
        daemonize()
        b += 1
        time.sleep(900)
