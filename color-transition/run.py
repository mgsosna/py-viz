import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import BoundaryNorm, ListedColormap, LinearSegmentedColormap
import sys

from helpers import gini, main_add_circles

cli_args = sys.argv

# Set start and end colors
if len(sys.argv) < 4:
    b_color = "#3bc9db"
    b_edgecolor = "#0c8599"
    #a_color = "#69db7c"
    #a_edgecolor = "#2f9e44"
    a_color = "#ff8787"
    a_edgecolor = "#e03131"
    #b_color = "#ffd43b"
    #b_edgecolor = "#f08c00"
else:
    a_edgecolor = sys.argv[1]
    a_color = sys.argv[2]
    b_edgecolor = sys.argv[3]
    b_color = sys.argv[4]

# Generate data
x = np.linspace(0, 1, 8000)
y = gini(x)

# We'll multiply by two so the circles aren't warped
points = np.array([x, 2*y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Generate plot
plt.figure(figsize=(5,5))
plt.xlim(-0.03, 1.03)
plt.ylim(-0.03, 1.03)
plt.xlabel("$p_\checkmark$", fontsize=16)
plt.ylabel("Gini impurity", fontsize=16)

# Overwrite tickmarks so they're accurate
plt.yticks(
    [0, 0.2, 0.4, 0.6, 0.8, 1.0],
    labels=[0, 0.1, 0.2, 0.3, 0.4, 0.5]
)

# Generate line
cmap = LinearSegmentedColormap.from_list(
    'custom',
    [a_edgecolor, b_edgecolor],
    N=1000
)
lc = LineCollection(segments, cmap=cmap,
    norm=plt.Normalize(0, 1))
lc.set_array(x)
lc.set_linewidth(5)
plt.gca().add_collection(lc)

# Add circles
main_add_circles(
    a_color=a_color,
    b_color=b_color,
    a_edgecolor=a_edgecolor,
    b_edgecolor=b_edgecolor
)

# Save figure
plt.savefig("gini_impurity5.png", dpi=400, bbox_inches='tight')
