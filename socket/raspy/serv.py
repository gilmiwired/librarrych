import socket
import cv2
import io
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('127.0.0.1', 50007))
    # 接続
    s.listen(1)
    # connection待
    while True:
        # アクセス時コネクションとアドレス交換
        conn, addr = s.accept()

        pic = cv2.imread("a.jpg")

        #画像のバイナリ化
        resized_img = cv2.resize(pic,(50,50))
        (status, encoded_img) = cv2.imencode('.jpg',pic, [int(cv2.IMWRITE_JPEG_QUALITY), IMAGE_QUALITY])
        print(type(encoded_img))
        print(encoded_img)

        packet_body = encoded_img.tostring()
        packet_header = len(packet_body).to_bytes(4, 'big')
        packet = packet_header + packet_body
        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if not data:
                    break
                print('data : {}, addr: {}'.format(data, addr))
                # conn.sendall(b'Received: ' + data)
                conn.sendall(b'Received:'+packet)
print('end')
