#using pillow lib
from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = '/editedImages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    cleanName = os.path.splitext(filename)[0]
    edit.save(f'.{pathOut}/{cleanName}_edited.png')