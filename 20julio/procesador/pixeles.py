from PIL import Image

img = Image.open("../logosinfondo/blastfury-rojo.png")
#convertimos a escala de RGBA
if img.mode != 'RGBA':
    img = img.convert('RGBA')

#print(datos)
width = img.size[0]
height = img.size[1]

pixeles = img.load()

#obtenemos todos los demás colores que no son los del fondo de la imagen
for x in range(1, width):
    for y in range(1, height):
        if pixeles[x, y] != (0, 0, 0, 255) and pixeles[x, y] != (0, 0, 0, 0):
            print(pixeles[x,y])

