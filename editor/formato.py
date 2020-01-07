from PIL import Image
#Abrimos la imagen original
img = Image.open("../21marzo2020/logoconfondo/Brutal_Crisis.jpg")
#La guardamos en formato PNG para su procesamiento
if img.format != 'PNG':
    img.save("../21marzo2020/logoconfondo/Brutal_Crisis.png")
    img.show()
    print("Imagen guardada con formato PNG")