import socket
import cv2
import io
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('127.0.0.1', 50007))
    # サーバにメッセージを送る
    s.sendall(b'hello mother fuckin beach')
    # ネットワークのバッファサイズは1024。
    data = s.recv(1024)

    
