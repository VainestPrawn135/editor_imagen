from PIL import Image

img = Image.open("../logoconfondo/blastfury-rojo.png")
#convertimos a escala de RGB, RGBA, L, HSV
if img.mode != 'RGBA':
    img = img.convert('RGBA')
datos = list(img.getdata()) # obtenemos los códigos de colores de cada píxel
#print(datos)
#img.save("prueba.png")
width = img.size[0]
height = img.size[1]
#print(width)
#print(height)

pixel = img.load()

#obtenemos todos los demás colores que no son los del fondo de la imagen
"""for x in range(0, width):
    for y in range(0, height):
        if pixel[x,y] != (247, 247, 247, 255):
            print(pixel[x,y])"""

r = g = b = 247
blanco = 255
while r <= blanco:
    while g <= blanco:
        while b <= blanco:
            for x in range(0, width):
                for y in range(0, height):
                    if pixel[x, y] == (r, g, b, 255):
                        pixel[x, y] = (0, 0, 0, 0)
            b+=1
        g+=1
    r+=1

"""codigo = 240
while codigo <= blanco:
    for x in range(0, width):
        for y in range(0, height):
            if pixel[x, y] == (codigo, codigo, codigo, 255):
                pixel[x, y] = (0, 0, 0, 0)
    codigo+=1"""

#acabamos de eliminar el fondo
img.show()
img.save("../logosinfondo/blastfury-rojo.png")
