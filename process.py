import sys
from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

import tkinter as tk
from tkinter import filedialog

from skimage import data
from skimage.feature import match_template
from skimage.io import imread, imsave
from skimage.transform import rotate

from file_ops import get_files
from calculations import *


parser = ArgumentParser()
parser.add_argument("-i", "--input", help="Input file")
parser.add_argument("-d", "--directory", help="Path to directory containing images to process")
parser.add_argument("-o", "--output", help="Path to output directory")

args = parser.parse_args()

# Load solar image
image = imread(args.input)
# Retrieve solar image dimensions
(image_width, image_height, image_depth) = image.shape

# Calculate the midpoint of the image
center_x = image_width / 2
center_y = image_height / 2

# Enter search coords
plt.figure()
plt.imshow(image) 
print("Insert coordinates of sunspot to scan for (integer)")
plt.show() 

x_start = int(input("x1: "))
x_end = int(input("x2: "))
y_start = int(input("y1: "))
y_end = int(input("y2: "))

# Retrieve center coordinates of sunspot
sunspot_center = get_midpoint(x_start, y_start, x_end, y_end)

# Retrieve sunspot to scan for
sunspot = image[y_start:y_end, x_start:x_end]
sunspot_height, sunspot_width, sunspot_depth = sunspot.shape

print("Sunspot to scan for")
plt.figure()
plt.imshow(sunspot) 
plt.show() 

for file in get_files(args.directory):
     # Load image to scan for sunspots
     scanable = imread(args.directory + '/' + file)

     # Get the results of the scan
     scanable_result = match_template(scanable, sunspot)
     ij = np.unravel_index(np.argmax(scanable_result), scanable_result.shape)

     x = ij[1]
     y = ij[0]

     # Retrieve center coordinates of scan result
     scanable_result_search_center = get_midpoint(x, y, x + sunspot_width, y + sunspot_height)

     # Calculate distance between center and sunspot result
     pyth_a = get_distance_between(center_x, center_y, scanable_result_search_center[0], scanable_result_search_center[1])
     # Calculate distance between center and sunspot
     pyth_b = get_distance_between(center_x, center_y, sunspot_center[0], sunspot_center[1])
     # Calculate distance between sunspot and sunspot result
     pyth_c = get_distance_between(scanable_result_search_center[0], scanable_result_search_center[1], sunspot_center[0], sunspot_center[1])

     slope = get_line_slope(center_x, center_y, sunspot_center[0], sunspot_center[1])
     intercept = get_line_intercept(center_x, center_y, slope)
     above = is_above(slope,intercept,scanable_result_search_center[0],scanable_result_search_center[1])
     above = not above if center_x > sunspot_center[0] else above

     rotate_by = (-1 if above else 1) * calculate_angle(pyth_a, pyth_b, pyth_c)
     rotated = rotate(scanable, rotate_by)

     imsave(args.output + '/' + file, rotated)