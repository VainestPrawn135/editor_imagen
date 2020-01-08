from PIL import Image
#Abrimos la imagen original
img = Image.open("../21marzo2020/logoconfondo/Diabolous.jpeg")
#La guardamos en formato PNG para su procesamiento
if img.format != 'PNG':
    img.save("../21marzo2020/logoconfondo/Diabolous.png")
    img.show()
    print("Imagen guardada con formato PNG")