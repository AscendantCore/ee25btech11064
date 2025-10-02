import matplotlib.pyplot as plt
import numpy as np

# Coordinates of the vertices of triangle ABC
A = np.array([0, 0])
B = np.array([5, 0])
C = np.array([2, 4])

# Midpoints of the sides
D = (A + B) / 2
E = (B + C) / 2
F = (C + A) / 2

# Plot the triangle ABC
fig, ax = plt.subplots()
triangle1 = plt.Polygon([A, D, F], fill=None, edgecolor='black', linewidth=2, zorder=2)
triangle2 = plt.Polygon([B, E, D], fill=None, edgecolor='blue', linewidth=2, zorder=2)
triangle3 = plt.Polygon([C, F, E], fill=None, edgecolor='brown', linewidth=2, zorder=2)
triangle4 = plt.Polygon([D, E, F], fill=None, edgecolor='darkgray', hatch='/', linestyle='--', linewidth=2, zorder=2)

# Plotting the triangle ABC and medial triangle DEF
ax.add_patch(triangle1)
ax.add_patch(triangle2)
ax.add_patch(triangle3)
ax.add_patch(triangle4)

# Plot the points A, B, C, D, E, F
ax.plot(A[0], A[1], 'go', ms=4)  # A
ax.plot(B[0], B[1], 'go', ms=4)  # B
ax.plot(C[0], C[1], 'go', ms=4)  # C
ax.plot(D[0], D[1], 'ro', ms=4)  # D
ax.plot(E[0], E[1], 'ro', ms=4)  # E
ax.plot(F[0], F[1], 'ro', ms=4)  # F

# Labels for points
ax.text(A[0], A[1], 'A', fontsize=12, ha='right', va='top')
ax.text(B[0], B[1], 'B', fontsize=12, ha='left', va='top')
ax.text(C[0], C[1], 'C', fontsize=12, ha='center', va='bottom')
ax.text(D[0], D[1]-0.1, 'D', fontsize=12, ha='center', va='top')
ax.text(E[0], E[1], 'E', fontsize=12, ha='left', va='bottom')
ax.text(F[0], F[1], 'F', fontsize=12, ha='right', va='bottom')

# Title and showing the plot
ax.set_aspect('equal')
ax.grid()
plt.xlim(-0.5, 5.5)
plt.ylim(-0.5, 4.5)
plt.title("Triangle ABC with Medial Triangle DEF")
plt.show()

