from pickle import TRUE
from turtle import fillcolor
from typing_extensions import dataclass_transform
import qrcode

data = 'linkedin.com/in/leonel-saavedra-2a13a2240'

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=TRUE)
img = qr.make_image(fill_color = 'cyan', back_color = 'white')

img.save('D:/Documents/Desktop/QR Proyect/Img/myqrcode1.png')