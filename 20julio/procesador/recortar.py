from PIL import Image

img = Image.open("../logosinfondo/blastfury-rojo.png")
#convertimos a escala de RGBA
if img.mode != 'RGBA':
    img = img.convert('RGBA')
datos = list(img.getdata()) # obtenemos los códigos de colores de cada píxel
#print(datos)
#img.save("prueba.png")
width = img.size[0]
height = img.size[1]
#print(width)
#print(height)
pixeles = img.load()

#obtenemos todos los demás colores que no son los del fondo de la imagen
"""for x in range(1, width):
    for y in range(1, height):
        if pixeles[x,y] != (247, 247, 247, 255):
            print(pixeles[x,y])"""

codigo_r = codigo_g = codigo_b = 100
while codigo_r <= 255:
    while codigo_g <= 255:
        while codigo_b <= 255:
            for x in range(0, width):
                for y in range(0, height):
                    if pixeles[x, y] == (codigo_r, codigo_g, codigo_b, 255):
                        pixeles[x, y] = (0, 0, 0, 0)
            codigo_b+=1
        codigo_g+=1
    codigo_r+=1

codigo = 100
while codigo <= 255:
    for x in range(0, width):
        for y in range(0, height):
            if pixeles[x, y] == (codigo, codigo, codigo, 255):
                pixeles[x, y] = (0, 0, 0, 0)
    codigo+=1

#acabamos de eliminar el fondo
img.show()
img.save("../logosinfondo/prueba.png")
