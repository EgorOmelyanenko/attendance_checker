import qrcode
import os

def generate_qr(path, string):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    os.makedirs("static/{}".format(path), exist_ok=True)
    img.save("static/{}/img.jpg".format(path))
