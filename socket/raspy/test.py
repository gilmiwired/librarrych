import io
from PIL import Image

tmpimg = Image.open("taki.png")
with io.BytesIO() as output:
    tmpimg.save(output,format="PNG")
    contents = output.getvalue()#バイナリ取得
    print(contents)#表示

img_from_str = Image.open(io.BytesIO(contents))
img_from_str.save('image_from_str2.png')
