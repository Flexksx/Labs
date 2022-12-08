import random 
from PIL import Image
count = 0
tries=100000
img = Image.open("hellobiden.png").convert('RGB')
for i in range(tries):
    p=img.getpixel((random.randint(0, img.width-1), random.randint(0, img.height-1)))
    if p == (255, 38, 0):
        count+=1

print(count/tries*42)
