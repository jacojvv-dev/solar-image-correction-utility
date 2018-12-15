import math
import numpy as np

def get_midpoint(x1, y1, x2, y2):
    return ((x1+x2)/2, (y1+y2)/2)

def get_distance_between(x1, y1, x2, y2):
    return math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

def calculate_angle(a, b, c):
    return np.arccos( (a ** 2 + b ** 2 - c ** 2) / (2 * a * b) ) * 180 / math.pi

def get_line_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def get_line_intercept(x1, y1, slope):
    return y1 - slope * x1

def is_above(slope, intercept, x, y):
    return y < slope * x + intercept