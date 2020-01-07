import itertools
import pandas as pd
from PIL import Image
from PIL import ImageDraw


data = {"TRACK_ID": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4],
        "x": [10, 75, 50, 300, 400, 12, 17, 27, 30, 45, 40, 15, 65, 400, 19, 45, 234],
        "Y": [10, 75, 50, 300, 500, 10, 105, 200, 100, 305, 420, 17, 47, 176, 20, 165, 375]}

df = pd.DataFrame(data)
df.set_index("TRACK_ID", inplace = True)


# Lo anterior es solo para crear un DataFraem como el tuyo,
# lo importante es lo siguiente:
tracks = df.groupby("TRACK_ID")

img = Image.new("RGB", (512,512), "black")
draw = ImageDraw.Draw(img)
colors = itertools.cycle(("Red", "Chartreuse", "DarkOrange", "DarkMagenta"))

for t, group in tracks:
    coords = tuple(zip(group.x, group.Y))
    draw.line(coords, width=2, fill=next(colors))


img.show()