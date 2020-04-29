from PIL import Image

img = Image.open("../7marzo20/logosinfondo/Eye_Of_Destruction_Nuevo.png")
#convertimos a escala de RGB, RGBA, L, HSV
if img.mode != 'RGBA':
    img = img.convert('RGBA')
datos = list(img.getdata())  # obtenemos los códigos de colores de cada píxel
width = img.size[0]
height = img.size[1]

print(width)
print(height)
print("Recortando sobrante")

pixel = img.load()

#esta parte del código parecerá sobrada porque hay más combinaciones de códigos de colores en las imágenes
for x in range(0, width):
    for y in range(0, height):
        if pixel[x, y] >= (0, 0, 0, 255):
            pixel[x, y] == (0, 0, 0, 0)

"""r = g = b = 200
a = 255
while r < a:
    while g < a:
        while b < a:
            for x in range(0, width):
                for y in range(0, height):
                    if pixel[x, y] >= (r, g, b, a):
                        pixel[x, y] = (0, 0, 0, 0)
            b+=1
        g+=1
    r+=1"""

"""a=255
while a >=0:
    for x in range(0, width):
        for y in range(0, height):
            if pixel[x, y] >= (255, 255, 253, a):
                pixel[x, y] == (0, 0, 0, 0)
    a-=1"""

#acabamos de eliminar el sobrante
img.show()
img.save("../7marzo20/logosinfondo/Temp.png")
