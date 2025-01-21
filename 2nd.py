import qrcode
from PIL import Image
import qrcode.constants

qr =qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10, border=4,)
qr.add_data("https://www.youtube.com/watch?v=yiYm1at49zs&pp=ygULcmFkaGUgcmFkaGE%3D")
qr.make(fit=True)
img = qr.make_image(fill_color = "red", back_color = "blue")
img.save("song_you.png")