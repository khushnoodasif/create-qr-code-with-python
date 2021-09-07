import pyqrcode 
from pyqrcode import QRCode

s = "https://blog.khushnoodasif.com"

qr = pyqrcode.create(s)

qr.svg("blog.svg", scale=7)
