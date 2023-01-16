import matplotlib.pyplot as plt
import numpy as np

# Coordinates of Emergency Center and City
emergency_center = np.array([0, 0, 0])
city = np.array([4, 5, 9])
coordinates = np.array([0, 0, 0])

# Calculate direction vector
direction_vector = city - emergency_center

# Define the parametric equation of the line
def parametric_equation(t):
    return emergency_center + t * direction_vector

# Generate values of t from 0 to 20
t = np.linspace(0, 20, 20)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Calculate the coordinates of the vehicle at each value of t
for i in t:
    coordinates = np.append(coordinates, [parametric_equation(i)])
    print(coordinates)

# Plot the interval
ax.plot(coordinates)

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()