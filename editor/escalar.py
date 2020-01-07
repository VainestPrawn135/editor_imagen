from PIL import Image
#Abrimos la imagen original
img = Image.open("../21marzo2020/logoconfondo/Brutal_Crisis.png")
#Escalamos la imagen
img = img.resize((1440,534), Image.ANTIALIAS)
#Guardamos
print("Imagen escalada y guardada")
img.show()
img.save("../21marzo2020/logoconfondo/Brutal_Crisis.png")