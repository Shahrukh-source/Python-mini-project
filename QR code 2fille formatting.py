# PIL using for formating qrcode image
# QRCode using for change the functionality of image
import qrcode
from PIL import Image

qr=qrcode.QRCode( version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://stackoverflow.com/questions/35850362/importerror-no-module-named-curses-when-trying-to-import-blessings")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
img.save("stack_overflow.png")