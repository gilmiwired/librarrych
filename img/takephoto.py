import time
import os
import sys
import subprocess
from multiprocessing import Process

subprocess.call(["rm","-r","top.jpg"])
subprocess.call(["bash","commit.sh"])
subprocess.call(["fswebcam","top.jpg","-q"])
subprocess.call(["bash","commit.sh"])
