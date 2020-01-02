from PIL import Image

img = Image.open("../21marzo2020/logoconfondo/Brutal_Crisis.png")
#convertimos a escala de RGB, RGBA, L, HSV
if img.mode != 'RGBA':
    img = img.convert('RGBA')
datos = list(img.getdata())  # obtenemos los códigos de colores de cada píxel
width = img.size[0]
height = img.size[1]

print(width)
print(height)

pixel = img.load()

#esta parte del código parecerá sobrada porque hay más combinaciones de códigos de colores en las imágenes
for x in range(0, width):
    for y in range(0, height):
        if pixel[x, y] == (254, 254, 254, 255):
            pixel[x, y] == (0, 0, 0, 0)


#acabamos de eliminar el sobrante
img.show()
img.save("../21marzo2020/logosinfondo/Brutal_Crisis.png")
