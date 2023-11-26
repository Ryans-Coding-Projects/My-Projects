import qrcode

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

data = input("Enter the url you want as a QR code: ")
qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color = "white")

img.save("qrcode.png")

print(f"QR code for {data} has been succefuly created! Find it in your current working directory.")
