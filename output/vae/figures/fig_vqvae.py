import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
for up in ("../../../scripts", "../../scripts"):
    p = os.path.normpath(os.path.join(HERE, up))
    if os.path.isdir(p): sys.path.insert(0, p); break
import figstyle as F

F.use_house_style()
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_title("VQ-VAE: Snapping to the nearest discrete vector", color=F.PALETTE["ink"], fontweight="bold")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

# Dictionary vectors
dict_pts = [(2, 8), (8, 8), (3, 2), (7, 2)]
for pt in dict_pts:
    ax.scatter([pt[0]], [pt[1]], color=F.PALETTE["purple"], marker="s", s=200)
    ax.text(pt[0]+0.5, pt[1]+0.5, "e_k", color=F.PALETTE["purple"], fontweight="bold")

# Continuous encoder output
z_pt = (3.5, 7.5)
ax.scatter([z_pt[0]], [z_pt[1]], color=F.PALETTE["blue"], s=150)
ax.text(z_pt[0]-0.5, z_pt[1]-0.5, "z_e(x)", color=F.PALETTE["blue"], fontweight="bold")

# Snap arrow
ax.annotate("", xy=dict_pts[0], xytext=z_pt,
            arrowprops=dict(arrowstyle="->", color=F.PALETTE["green"], lw=2))
ax.text(2.5, 7.2, "snap", color=F.PALETTE["green"], fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(HERE, "fig_vqvae.png"), dpi=150, bbox_inches="tight")
plt.close()
