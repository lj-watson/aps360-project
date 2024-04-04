"""
@brief Given image folder with their location "x_y.png" in the name, rearrange them
from left to right
"""

import os
import json

def get_position_from_filename(filename):
    # Returns the (x, y) position from the given file
    base = os.path.basename(filename)  # Extracts filename from path
    name, ext = os.path.splitext(base)  # Separates the extension
    if "_" in name and ext == ".png":
        try:
            x, y = map(int, name.split("_"))
            return x, y
        except ValueError:
            pass
    return None

# Get the image directory path
while True:
    img_dir = input("Enter directory path to be classified: ")
    if not img_dir or not os.path.isdir(img_dir):
        print("Invalid input, try again")
    else:
        break

# Extract positions
positions = []
for filename in os.listdir(img_dir):
    pos = get_position_from_filename(filename)
    if pos:
        positions.append((pos, filename))

# Sort images based on the x position
positions.sort()

# Rearrange the directory
y_values = []
for i, ((x, y), filename) in enumerate(positions, 1):
    new_name = f"{i:03d}.png"
    old_path = os.path.join(img_dir, filename)
    new_path = os.path.join(img_dir, new_name)
    os.rename(old_path, new_path)
    y_values.append(y)

# Write y values to json file
filename = 'symbol_y_values.json'
output_path = "../audio"
json_path = f'{output_path}/{filename}'
with open(json_path, 'w') as file:
    json.dump(y_values, file)