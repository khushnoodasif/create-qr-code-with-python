import pyqrcode
from pyqrcode import QRCode

#String that represent the QR Code
s = "https://khushnoodasif.com"

#Genreating QR Code
qr = pyqrcode.create(s)

#Saving QR Code in .svg format
qr.svg("website.svg",scale = 7)
