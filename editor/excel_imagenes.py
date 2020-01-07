from openpyxl import Workbook
from PIL import Image

img = Image.open("../21marzo2020/logoconfondo/blastfury-blanco.png")
#convertimos a escala de RGB, RGBA, L, HSV
if img.mode != 'RGBA':
    img = img.convert('RGBA')
datos = list(img.getdata())  # obtenemos los códigos de colores de cada píxel
width = img.size[0]
height = img.size[1]

wb = Workbook()
ruta = 'datos.xlsx'

hoja = wb.active
hoja.title = "Pixeles_Imagen"

#fila = 1 #Fila donde empezamos
#col_fecha = 1 #Columna donde guardamos las fechas
#col_dato = 2 #Columna donde guardamos el dato asociados a cada fecha

for row in datos:
    hoja.append(row)

wb.save(filename = ruta)