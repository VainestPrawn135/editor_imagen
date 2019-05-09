from PIL import Image

img = Image.open("../logosinfondo/blastfury-rojo.png")
#convertimos a escala de RGBA
if img.mode != 'RGBA':
    img = img.convert('RGBA')
datos = list(img.getdata())  # obtenemos los códigos de colores de cada píxel
print(datos)
