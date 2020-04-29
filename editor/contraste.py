from PIL import Image, ImageEnhance

img = Image.open("../7marzo20/logosinfondo/Eye_Of_Destruction.png")
#convertimos a escala de RGB, RGBA, L, HSV
print("Escala de la imagen de entrada:", img.mode)
contrast = ImageEnhance.Contrast(img)
print("Modificando contraste...")
#Contraste normal
#img.show()
#Sale la imagen ya con el contraste modificado
img = contrast.enhance(8)
img.show()
img.save("../7marzo20/logosinfondo/Eye_Of_Destruction_Nuevo.png")