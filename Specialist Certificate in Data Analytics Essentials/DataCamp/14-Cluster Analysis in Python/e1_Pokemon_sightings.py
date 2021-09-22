"""
Pokémon sightings
There have been reports of sightings of rare, legendary Pokémon. You have been asked to investigate!
Plot the coordinates of sightings to find out where the Pokémon might be.
The X and Y coordinates of the points are stored in list x and y, respectively.

Instructions
100 XP

    Import the pyplot class from matplotlib library as plt.
    Create a scatter plot using the pyplot class.
    Display the scatter plot created in the earlier step.

"""

# Import plotting class from matplotlib library
import matplotlib.pyplot as plt

x = [9, 6, 2, 3, 1, 7, 1, 6, 1, 7, 23, 26, 25, 23, 21, 23, 23, 20, 30, 23]
y = [8, 4, 10, 6, 0, 4, 10, 10, 6, 1, 29, 25, 30, 29, 29, 30, 25, 27, 26, 30]

# Create a scatter plot
plt.scatter(x, y)

# Display the scatter plot
plt.show()