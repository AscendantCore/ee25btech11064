import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Ellipse parameters
a = 3  # semi-major axis
b = np.sqrt(5)  # semi-minor axis

# Generate points for the ellipse
theta = np.linspace(0, 2 * np.pi, 400)
x = a * np.cos(theta)
y = b * np.sin(theta)

# Points for the latus rectum
latus_rectum_points = [(2, 5/3), (2, -5/3), (-2, 5/3), (-2, -5/3)]

# Tangent line equation function
def tangent_line(x1, y1):
    """Return the equation of the tangent line at (x1, y1) on the ellipse."""
    return lambda x: (1 - (x * x1 / a**2)) * (b**2 / y1)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the ellipse
ax.plot(x, y, color="blue")
ellipse = Line2D([0], [0], color='b')

#Mark the Latera Recta
ax.plot([2, 2], [-5/3, 5/3], 'r--')
ax.plot([-2, -2], [-5/3, 5/3], 'r--')
latera_recta = Line2D([0], [0], color='r', linestyle='-')

# Mark and label the latus rectum points with two decimal places
for (x1, y1) in latus_rectum_points:
    ax.plot(x1, y1, 'ro')  # Mark the point
    ax.text(x1+0.8*(x1/np.abs(x1)), y1+0.2*(y1/np.abs(y1)), f'({x1:.2f}, {y1:.2f})', fontsize=12, ha='center', va='center')

# Plot tangents at the endpoints of the latus rectum
for (x1, y1) in latus_rectum_points:
    # Get tangent function
    tangent = tangent_line(x1, y1)
    
    # Create x values for the tangent lines
    x_vals = np.linspace(-5, 5, 100)
    y_vals = tangent(x_vals)  # Calculate corresponding y values
    
    # Plot the tangent lines
    ax.plot(x_vals, y_vals, 'g--')
    
    #Fill in the quadrilateral
    quad_x = np.linspace(0, 4.5, 90) if x1>0 else np.linspace(-4.5, 0, 90)
    quad_y1 = tangent(quad_x)
    plt.fill_between(quad_x, quad_y1, color='gray', alpha=0.2)
tangents = Line2D([0], [0], color='g', linestyle='-')

# Set axes limits
ax.set_xlim(-5, 5)
ax.set_ylim(-3.5, 3.5)

# Add labels and title
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_title("Ellipse, Latera Recta, and Tangents")

# Show grid
ax.grid(True)

# Show the plot
plt.legend(handles=[ellipse, latera_recta, tangents], labels=['Ellipse: $\\frac{x^2}{9} + \\frac{y^2}{5} = 1$', 'Latera Recta', 'Tangents'])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

