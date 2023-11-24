import qrcode #imported module of pip packages in python
qr=qrcode.QRCode(
   version=15,
   box_size=10,
   border=5
)

data="" #social media links
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white") # give them a more attribute or make changes in the future
img.save('')  # save it in png format


