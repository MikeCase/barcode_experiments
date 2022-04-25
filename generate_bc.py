from barcode import Code128

data = "https://mikecase.us"

mybc = Code128(data)

mybc.save('mikecase.us.png')