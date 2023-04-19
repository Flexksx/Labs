import numpy as np

with open("C:\\Users\\Cristi\\Documents\\GitHub\\Labs\\LabsNA\\Labs1NA\\fotka.png", "rb") as image:
  f = image.read()
  b = bytearray(f)

for i in b:
  print(i)