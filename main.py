import qrcode

# URL du fichier PDF hébergé
url_pdf = "https://drive.google.com/file/d/1z9NZL5yEjI7RRIYqQlNJ3ox1XNa--oB6/view?usp=sharing"

# Générer le QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url_pdf)
qr.make(fit=True)

# Créer une image pour le QR Code
img = qr.make_image(fill='black', back_color='white')
img.save("menu_qr_code.png")
