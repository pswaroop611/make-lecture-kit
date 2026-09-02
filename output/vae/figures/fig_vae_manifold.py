import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
for up in ("../../../scripts", "../../scripts"):
    p = os.path.normpath(os.path.join(HERE, up))
    if os.path.isdir(p): sys.path.insert(0, p); break
import figstyle as F

F.contour(
    lambda x, y: np.exp(-(x**2 + y**2)/2) + 0.5 * np.exp(-((x-2)**2 + (y-2)**2)/2),
    (-3, 4), (-3, 4),
    "Variational Autoencoder: Overlapping Gaussian clouds create a continuous manifold.",
    points=[(0, 0, "z1", "X"), (2, 2, "z2", "o")],
    out=os.path.join(HERE, "fig_vae_manifold.png")
)
