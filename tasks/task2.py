from PIL import Image
import os

directory = r'C:\Users\luixh\Documents\SpartaGlobal\Github\python_learning\Pictures'
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        filepath = os.path.join(directory, filename)  # Construct the full path to the image file
        prefix = filename.split(".jpg")[0]
        im = Image.open(filepath)  # Open the image using the full path
        im.save(os.path.join(directory, prefix + '.png'))
    else:
        continue

