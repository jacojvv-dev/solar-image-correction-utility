import math
import numpy as np

def get_midpoint(x1, y1, x2, y2):
    """
    Returns the midpoint between two coordinates
    https://www.mathsisfun.com/algebra/line-midpoint.html
    """
    return ((x1+x2)/2, (y1+y2)/2)

def get_distance_between(x1, y1, x2, y2):
    """
    Returns the distance between two coordinates
    https://www.mathwarehouse.com/algebra/distance_formula/index.php
    """
    return math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

def calculate_angle(a, b, c):
    """
    Returns angle C in degrees using the lengths of the known edges
    https://www.calculator.net/triangle-calculator.html
    """
    return np.arccos( (a ** 2 + b ** 2 - c ** 2) / (2 * a * b) ) * 180 / math.pi

def get_line_slope(x1, y1, x2, y2):
    """
    Returns the slope of a line using two known coordinates
    https://www.calculator.net/slope-calculator.html
    """
    return (y2 - y1) / (x2 - x1)

def get_line_intercept(x1, y1, slope):
    """
    Returns the intercept on a line where the coordinate and slope is known
    https://www.chilimath.com/lessons/intermediate-algebra/slope-intercept-form/
    """
    # y1 = (slope * x1) + b -> y1 - (slope * x1) = b
    return y1 - slope * x1

def is_above(slope, intercept, x, y):
    """
    Returns true if a coordinate is above a line
    """
    return y < slope * x + intercept