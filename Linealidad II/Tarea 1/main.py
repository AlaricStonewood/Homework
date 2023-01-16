import matplotlib.pyplot as plt

# This script was created to display a coordinate system for Homework 1 of
# Linealidad II using chat.openai.com as an assistant

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# City
ax.scatter(0, 0, 0, c='r', marker='o', label='City')

# Forest
ax.scatter(10, 8, -7, c='g', marker='^', label='Forest')

# Highways
ax.scatter(-8, -7, -4, c='black', marker='s', label='Highway')
ax.scatter(10, 2, 1, c='black', marker='s')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

plt.show()
