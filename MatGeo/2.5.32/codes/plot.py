import matplotlib.pyplot as plt

# Vertices of the triangle
A = (7, 10)
B = (-2, 5)
C = (3, 4)

# Midpoints of sides
D = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
E = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
F = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)

# Plotting the triangle and midpoints
fig, ax = plt.subplots()

# Plot the triangle ABC
triangle = plt.Polygon([A, B, C], closed=True, fill=None, edgecolor='black', label='Triangle ABC')

# Plot the midpoints D, E, F
ax.scatter(*zip(A, B, C, D, E, F), color='gray')
ax.text(A[0], A[1], 'A', fontsize=12, ha='left', va='top', color='g')
ax.text(B[0], B[1], 'B', fontsize=12, ha='right', va='top', color='r')
ax.text(C[0], C[1], 'C', fontsize=12, ha='left', va='top', color='b')
ax.text(D[0], D[1], 'D', fontsize=12, ha='right', va='bottom', color='b')
ax.text(E[0], E[1], 'E', fontsize=12, ha='right', va='bottom', color='g')
ax.text(F[0], F[1], 'F', fontsize=12, ha='right', va='bottom', color='r')

# Plot the medians AD, BE, CF
plt.plot([A[0], E[0]], [A[1], E[1]], color='g', label='Median AE')
plt.plot([B[0], F[0]], [B[1], F[1]], color='r', label='Median BF')
plt.plot([C[0], D[0]], [C[1], D[1]], color='b', label='Median CD')

# Labels and settings
ax.add_patch(triangle)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.title('Triangle ABC with Midpoints and Medians')
plt.grid(True)
plt.legend()
plt.show()

