import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Jelen Kriz Angel P. Mampusti live in New You City. 24 years old, CEO of JJJ Corporation")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="violet")
img.save("JKAM.png")