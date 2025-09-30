import numpy as np
import matplotlib.pyplot as plt

# Parameters of the ellipse
a = 5  # semi-major axis
b = 1  # semi-minor axis

# Parametric equations of ellipse
# Generate theta values
theta = np.linspace(0, 2*np.pi, 400)
y = a * np.sin(theta)
x = b * np.cos(theta)

# Plot ellipse
plt.plot(x, y, label=r"$x^2+\frac{y^2}{25}=1$")

# Mark ends of the axes
plt.scatter([0, 0], [5, -5], color="blue", zorder=5, label="Major ends")
plt.scatter([1, -1], [0, 0], color="red", zorder=5, label="Minor ends")

# Add annotations
plt.text(1.1, 0.1, "(1,0)", color="red")
plt.text(-2.3, 0.1, "(-1,0)", color="red")
plt.text(0.1, 5.1, "(0,5)", color="blue")
plt.text(0.1, -5.3, "(0,-5)", color="blue")

# Axes setup
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.gca().set_aspect('equal')
plt.legend(loc='upper right')
plt.title("Ellipse with Major-Axis and Minor-Axis Ends")
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid(True)
plt.show()
