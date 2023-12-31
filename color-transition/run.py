import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import BoundaryNorm, ListedColormap, LinearSegmentedColormap

from helpers import gini, main_add_circles

# Set start and end colors
a_color = "#0c8599"
b_color = "#f08c00"

x = np.linspace(0, 1, 8000)
y = gini(x)

# We'll multiply by two so the circles aren't warped
points = np.array([x, 2*y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

cmap = LinearSegmentedColormap.from_list('custom blue', [a_color, b_color], N=1000)

# Generate plot
plt.figure(figsize=(5,5))
lc = LineCollection(segments, cmap=cmap,
    norm=plt.Normalize(0, 1))
lc.set_array(x)
lc.set_linewidth(3)

plt.xlim(-0.03, 1.03)
plt.ylim(-0.03, 1.03)
plt.gca().add_collection(lc)

plt.xlabel("$p_▲$", fontsize=16)
plt.ylabel("Gini impurity", fontsize=16)

# Overwrite tickmarks
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], labels=[0, 0.1, 0.2, 0.3, 0.4, 0.5])

# Add circles
main_add_circles(a_color, b_color)

plt.savefig("gini_impurity.png", dpi=400, bbox_inches='tight')
