import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

# Define the equations
def plane1(x, y):
    return 4 - x - 2 * y

def plane2(x, y):
    return (5 - 2*x - y) / 2

def plane3(x, y):
    return 1 - x + y

# Create meshgrid for x and y
x_vals = np.linspace(-5, 5, 10)
y_vals = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x_vals, y_vals)

# Compute Z values for each plane
Z1 = plane1(X, Y)
Z2 = plane2(X, Y)
Z3 = plane3(X, Y)

# Plotting the planes and solution
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each plane
surf1 = ax.plot_surface(X, Y, Z1, color='blue', alpha=0.5, rstride=100, cstride=100)
surf2 = ax.plot_surface(X, Y, Z2, color='green', alpha=0.5, rstride=100, cstride=100)
surf3 = ax.plot_surface(X, Y, Z3, color='red', alpha=0.5, rstride=100, cstride=100)

# Plot the solution line (x = 2 - z, y = 1)
z_vals = np.linspace(-5, 5, 10)
x_sol = 2 - z_vals
y_sol = np.ones_like(z_vals)

line = ax.plot(x_sol, y_sol, z_vals, color='black', label='Solution Line')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('System of Equations and their Solution')

# Manually add legend
ax.legend(handles=[
    Line2D([0], [0], color='blue', lw=4, label=r'$x + 2y + z = 4$'),
    Line2D([0], [0], color='green', lw=4, label=r'$2x + y + 2z = 5$'),
    Line2D([0], [0], color='red', lw=4, label=r'$x - y + z = 1$'),
    Line2D([0], [0], color='black', lw=4, label='Solution Line')
])

# Show the plot
ax.view_init(30, -30)
plt.show()

