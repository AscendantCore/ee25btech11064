import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the lines with their parametric equations
# Define the parametric values for kappa_1 and kappa_2
kappa_1_vals = np.linspace(-5, 5, 50)
kappa_2_vals = np.linspace(-5, 5, 50)
# Parametric equations of the lines
r1 = np.array([1, 2, 1]) + kappa_1_vals[:, None] * np.array([1, -1, 1])
r2 = np.array([2, -1, -1]) + kappa_2_vals[:, None] * np.array([2, 1, 2])

# Plot the lines
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Plot line 1
ax.plot(r1[:, 0], r1[:, 1], r1[:, 2], label='Line 1', color='blue')
# Plot line 2
ax.plot(r2[:, 0], r2[:, 1], r2[:, 2], label='Line 2', color='red')

# Points of closest approach on both lines
closest_point_1 = np.array([17/6,1/6,17/6])
closest_point_2 = np.array([26/6,1/6,8/6])

# Mark the vector along points of closest approach
closest_line_vals = np.linspace(0, 1, 10)
closest_line = np.array([17/6,1/6,17/6]) + closest_line_vals[:, None] * np.array([3/2,0,-3/2])
ax.plot(closest_line[:, 0], closest_line[:, 1], closest_line[:, 2], label='Line of closest approach', color='green')

# Mark the points of closest approach
ax.scatter(closest_point_1[0], closest_point_1[1], closest_point_1[2], color='purple', s=10, label='Closest Point on Line 1')
ax.scatter(closest_point_2[0], closest_point_2[1], closest_point_2[2], color='orange', s=10, label='Closest Point on Line 2')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of Two Lines and Points of Closest Approach')

# Set the camera angle
ax.view_init(elev=10, azim=45)

# Show the plot
ax.legend()
plt.show()

