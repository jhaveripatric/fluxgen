import qrcode
from PIL import Image

data = "https://contact.fluxgenindustries.ca/bhargav"

qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Generate image with white bg then convert white to transparent
img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Make white background fully transparent
datas = img.getdata()
new_data = []
for item in datas:
    if item[:3] == (255, 255, 255):  # white becomes transparent
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)

path = "./fluxgen_bhargav_qr.png"
img.save(path)