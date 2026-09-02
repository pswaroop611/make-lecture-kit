import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
for up in ("../../../scripts", "../../scripts"):
    p = os.path.normpath(os.path.join(HERE, up))
    if os.path.isdir(p): sys.path.insert(0, p); break
import figstyle as F

F.use_house_style()
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_title("Beta-VAE: Disentangled axes", color=F.PALETTE["ink"], fontweight="bold")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# draw axes
ax.axhline(0, color=F.PALETTE["muted"], linewidth=1)
ax.axvline(0, color=F.PALETTE["muted"], linewidth=1)

ax.text(2.5, 0.2, "Smile", color=F.PALETTE["blue"], fontweight="bold")
ax.text(0.2, 2.5, "Azimuth", color=F.PALETTE["purple"], fontweight="bold")

# draw points along axes
ax.scatter([1, 2, -1, -2], [0, 0, 0, 0], color=F.PALETTE["blue"], s=100)
ax.scatter([0, 0, 0, 0], [1, 2, -1, -2], color=F.PALETTE["purple"], s=100)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(os.path.join(HERE, "fig_beta_vae.png"), dpi=150, bbox_inches="tight")
plt.close()
