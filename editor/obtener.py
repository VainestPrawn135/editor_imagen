from PIL import Image

img = Image.open("../7marzo20/logosinfondo/FFM.png")
#convertimos a escala de RGBA
if img.mode != 'RGBA':
    img = img.convert('RGBA')
datos = list(img.getdata())  # obtenemos los códigos de colores de cada píxel
#print(datos)
archivo = open("datos.txt", "w")
archivo.write(" ".join(datos.__str__())+"\n")
archivo.close()

color = list(img.getbands())
print(color)

img.show()
