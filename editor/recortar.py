from PIL import Image

img = Image.open("../22mayo/logo_mors.png")
#convertimos a escala de RGB, RGBA, L, HSV
print("Escala de la imagen de entrada:", img.mode)

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
print("Escala de la imagen de salida:" ,img.mode)

#obtenemos todos los demás colores que no son los del fondo de la imagen
"""for x in range(0, width):
    for y in range(0, height):
        if pixel[x,y] != (247, 247, 247, 255):
            print(pixel[x,y])"""

#obtenemos todos los demás colores que son los del fondo de la imagen y los hacemos transparentes
"""for x in range(0, width):
    for y in range(0, height):
        if pixel[x,y] == (255, 254, 255, 255):
            pixel[x,y] = (0, 0, 0, 0)"""

r = g = b = 0
a = 255
while r < a:
    while g < a:
        while b < a:
            for x in range(0, width):
                for y in range(0, height):
                    if pixel[x, y] >= (r, g, b, a):
                        pixel[x, y] = (255, 255, 255, 0)
            b+=1
        g+=1
    r+=1

"""codigo = 0
a = 255
while codigo < 3:
    for x in range(0, width):
        for y in range(0, height):
            if pixel[x, y] <= (codigo, codigo, codigo, a):
                pixel[x, y] = (0, 0, 0, 0)
    codigo+=1"""

#acabamos de eliminar el fondo
img.show()
#img.save("../22mayo/logo_mors.png")
