import qrcode

qr = qrcode.QRCode()

link_data = "https://mikecase.us"
qr.add_data(link_data)

qr.make(fit=True)
img = qr.make_image()
img.save('mikecase.us.png')
