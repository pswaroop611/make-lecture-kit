import os, sys
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
for up in ("../../../scripts", "../../scripts"):
    p = os.path.normpath(os.path.join(HERE, up))
    if os.path.isdir(p): sys.path.insert(0, p); break
import figstyle as F

F.use_house_style()

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

# Standard Autoencoder (left)
ax = axes[0]
ax.set_title("Standard Autoencoder", color=F.PALETTE["ink"], fontweight="bold")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

# Draw gaps and irregular clusters
ax.scatter([3, 3.5, 2.5], [7, 7.5, 6.5], color=F.PALETTE["blue"], s=200, alpha=0.7)
ax.scatter([7, 7.5, 6.5], [3, 2.5, 3.5], color=F.PALETTE["purple"], s=200, alpha=0.7)
ax.scatter([8, 8.5, 7.5], [8, 8.5, 7.5], color=F.PALETTE["amber"], s=200, alpha=0.7)

ax.text(5, 5, "? GAP ?", ha="center", va="center", color=F.PALETTE["red"], fontweight="bold")

# Variational Autoencoder (right)
ax2 = axes[1]
ax2.set_title("Variational Autoencoder", color=F.PALETTE["ink"], fontweight="bold")
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis("off")

# Draw overlapping smooth distributions
from matplotlib.patches import Ellipse
e1 = Ellipse((4, 6), width=5, height=5, color=F.PALETTE["blue"], alpha=0.3)
e2 = Ellipse((6, 4), width=5, height=5, color=F.PALETTE["purple"], alpha=0.3)
e3 = Ellipse((6, 7), width=5, height=5, color=F.PALETTE["amber"], alpha=0.3)
ax2.add_patch(e1)
ax2.add_patch(e2)
ax2.add_patch(e3)

ax2.text(5, 5, "Smooth transition", ha="center", va="center", color=F.PALETTE["green"], fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(HERE, "fig_autoencoder.png"), dpi=150, bbox_inches="tight")
plt.close()
