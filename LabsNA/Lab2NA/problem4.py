import numpy as np
import math

# Parse the dataset
data = {}
with open('LabsNA\\Lab2NA\\Assets\\map.txt') as file:
    for line in file:
        coord_str, elevation_str = line.strip().split('            ')
        coord = tuple(map(int, coord_str.strip('()').split(', ')))
        if 'NaN' in elevation_str:
            elevation = float('nan')
        else:
            elevation = float(elevation_str)
        data[coord] = elevation

# Define the IDW function
def inverse_distance_weighting(coord, data, p=2):
    weights = []
    elevations = []
    for c, e in data.items():
        if not math.isnan(e):  # Only consider known points
            d = math.sqrt((coord[0]-c[0])**2 + (coord[1]-c[1])**2)
            if d > 0:  # Avoid division by zero
                weight = 1 / d**p
                weights.append(weight)
                elevations.append(e * weight)
    
    if not weights:
        return None
    return sum(elevations) / sum(weights)

for coord, elevation in data.items():
    if math.isnan(elevation):
        data[coord] = inverse_distance_weighting(coord, data)

for i in data:
    print(i, data[i])