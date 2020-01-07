from PIL import Image

img = Image.open("../21marzo2020/logoconfondo/Brutal_Crisis.png")
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

#obtenemos todos los demás colores que son los del fondo de la imagen y los hacemos transparentes
"""for x in range(0, width):
    for y in range(0, height):
        if pixel[x,y] == (255, 254, 255, 255):
            pixel[x,y] = (255, 255, 255, 255)"""

r = g = b = 253
a = 255
while r < a:
    while g < a:
        while b < a:
            for x in range(0, width):
                for y in range(0, height):
                    if pixel[x, y] == (r, g, b, 253) or (r, g, b, 254):
                        pixel[x, y] = (255, 255, 255, 255)
            b+=1
        g+=1
    r+=1

#acabamos de eliminar el fondo
img.show()
img.save("../21marzo2020/logoconfondo/Brutal_Crisis_temp.png")