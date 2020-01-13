from PIL import Image
#Abrimos la imagen original
img = Image.open("../7marzo2020/logoconfondo/Eye_Of_Destruction.jpeg")
#La guardamos en formato PNG para su procesamiento
if img.format != 'PNG':
    img.save("../7marzo2020/logoconfondo/Eye_Of_Destruction.png")
    img.show()
    print("Imagen guardada con formato PNG")