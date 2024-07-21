from model import ColorPredictor
import cv2 as cv

namer = ColorPredictor()

img = cv.imread("Nail.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

preds = []
for row in img:
    for px in row:
        preds.append(namer.predict(px))

for color in ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'white', 'gray', 'black']:
    print(f"{color}: {preds.count(color)}")