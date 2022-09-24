import qrcode

img = qrcode.make("Hi hello")
img.save("hi.jpg")