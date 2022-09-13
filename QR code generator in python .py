# make function build qrcode
# safe function given qrcode in the png form(image)
import qrcode as qr
img = qr.make("https://stackoverflow.com/questions/35850362/importerror-no-module-named-curses-when-trying-to-import-blessings")
img.save("stack_overflow.png")
