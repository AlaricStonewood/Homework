import matplotlib.pyplot as plt

# This script was created to display a coordinate system for Homework 1 of Linealidad II

# Coordinates of locations
emergency_center = [0, 0, 0]
drone_response_city = [2, 3, 5]
drone_response_forest = [5, 8, -4]
drone_response_highway_A1 = [-4, -4, -2]
drone_response_highway_A2 = [5, 1, 1]
city = [4, 5, 9]
forest = [10, 8, -7]
highway_A1 = [-8, -7, -4]
highway_A2 = [10, 2, 1]

# Plot the locations on a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(emergency_center[0], emergency_center[1], emergency_center[2], c='r', marker='P', label='Emergency Center')
ax.scatter(city[0], city[1], city[2], c='b', marker='p', label='City')
ax.scatter(forest[0], forest[1], forest[2], c='g', marker='^', label='Forest')
ax.scatter(highway_A1[0], highway_A1[1], highway_A1[2], c='y', marker='s', label='Highway A1')
ax.scatter(highway_A2[0], highway_A2[1], highway_A2[2], c='c', marker='s', label='Highway A2')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
# plt.show()

# Plot with 4 quick reaction drones
ax.scatter(drone_response_city[0], drone_response_city[1],
           drone_response_city[2], c='b', marker='+', label='Quick_Response_City')
ax.scatter(drone_response_forest[0], drone_response_forest[1],
           drone_response_forest[2], c='g', marker='+', label='Quick_Response_Forest')
ax.scatter(drone_response_highway_A1[0], drone_response_highway_A1[1],
           drone_response_highway_A1[2], c='y', marker='+', label='Quick_Response_Highway A1')
ax.scatter(drone_response_highway_A2[0], drone_response_highway_A2[1],
           drone_response_highway_A2[2], c='c', marker='+', label='Quick_Response_Highway A2')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.plot((drone_response_city[0], drone_response_city[1],
           drone_response_city[2]), (city[0], city[1], city[2]), linestyle="--")
# Show the plot with reaction drones
plt.show()


