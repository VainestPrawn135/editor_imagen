from PIL import Image
#Abrimos la imagen original
img = Image.open("../7marzo20/logoconfondo/Demolition.jpg")
#La guardamos en formato PNG para su procesamiento
if img.format != 'PNG':
    img.save("../7marzo20/logoconfondo/Demolition.png")
    img.show()
    print("Imagen guardada con formato PNG")