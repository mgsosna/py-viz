import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def hex_to_rgb(color: str) -> tuple:
    """
    Converts a hex color (e.g., '#1971c2') to RGB ((25, 113, 194))
    """
    color = color[1:] # remove leading #
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(color: tuple) -> str:
    """
    Converts an RGB color to hex.
    """
    return '#%02x%02x%02x' % color

def interpolate(a_hex: str, b_hex: str, n: int) -> list:
    """
    Generate a list of hex colors that gradually transition from
    the first to last color.
    """
    a_rgb = hex_to_rgb(a_hex)
    b_rgb = hex_to_rgb(b_hex)

    rgb_array = np.linspace(a_rgb, b_rgb, n).astype(int)

    return [rgb_to_hex(tuple(row)) for row in rgb_array]

def gini(pk: float) -> float:
    """
    Calculate Gini impurity given a probability of randomly
    selecting an element belonging to class k (out of 2 classes).
    """
    return 1 - pk**2 - (1-pk)**2

def plot_circle(x: float, y: float, edgecolor: str, dict_list: list) -> Circle:
    plt.text(x-0.08, y, **dict_list[0])
    plt.text(x+0.005, y+0.015, **dict_list[1])
    plt.text(x+0.04, y-0.03, **dict_list[2])
    plt.text(x, y-0.06, **dict_list[3])
    plt.text(x-0.035, y+0.04, **dict_list[4])
    plt.text(x-0.035, y-0.015, **dict_list[5])
    plt.text(x-0.052, y-0.065, **dict_list[6])
    plt.text(x+0.042, y+0.03, **dict_list[7])
    return plt.Circle((x, y), 0.1, edgecolor=edgecolor, lw=2, fill=False)

def main_add_circles(a_color = '#1971c2', b_color= '#e03131') -> None:
    a_sign = "■"
    b_sign = "▲"
    a_fontsize = 10
    b_fontsize = 12

    a_dict = {"s": a_sign, "color": a_color, "fontsize": a_fontsize}
    b_dict = {"s": b_sign, "color": b_color, "fontsize": b_fontsize}

    cir_colors = interpolate(a_color, b_color, 5)

    # Left
    circle1 = plot_circle(0.15, 0.09, cir_colors[0], [a_dict]*8)
    circle2 = plot_circle(0.28, 0.5, cir_colors[1], [a_dict] + [b_dict]*2 + [a_dict]*5)
    circle3 = plot_circle(0.5, 0.88, cir_colors[2], [a_dict] + [b_dict]*4 + [a_dict]*3)
    circle4 = plot_circle(0.72, 0.5, cir_colors[3], [a_dict] + [b_dict]*6 + [a_dict])
    circle5 = plot_circle(0.85, 0.09, cir_colors[4], [b_dict]*8)

    # Add nodes
    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    plt.gca().add_patch(circle3)
    plt.gca().add_patch(circle4)
    plt.gca().add_patch(circle5)
