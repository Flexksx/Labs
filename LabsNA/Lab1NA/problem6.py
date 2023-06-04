from PIL import Image
import numpy as np

img=Image.open("C:\\Users\\Cristi\\Documents\\GitHub\\Labs\\LabsNA\\Lab1NA\\fotka.png")
width=img.size[0]
height=img.size[1]

pixel_matrix=[[0 for i in range(width)] for j in range(height)]
for i in range(width):
    for j in range(height):
        pixel_matrix[i][j]=img.getpixel((i,j))
