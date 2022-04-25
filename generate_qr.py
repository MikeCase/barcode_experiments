import qrcode

qr = qrcode.QRCode()

link_data = "https://ptainer.splaq.us"
qr.add_data(link_data)

qr.make(fit=True)
img = qr.make_image()
img.save('splaq.us.png')
