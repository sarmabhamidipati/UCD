"""
Extract RGB values from image
There are broadly three steps to find the dominant colors in an image:

    Extract RGB values into three lists.
    Perform k-means clustering on scaled RGB values.
    Display the colors of cluster centers.

To extract RGB values, we use the imread() function of the image class of matplotlib.
Empty lists, r, g and b have been initialized.
Instructions
100 XP

    Import image class of matplotlib.
    Read the image using the imread() function and print the dimensions of the resultant matrix.
    Store the values for the three colors from all pixels in lists r, g and b.

"""
# Import image class of matplotlib
import matplotlib.image as img

r = []
g = []
b = []

# Read batman image and print dimensions
batman_image = img.imread('batman.jpg')
print(batman_image.shape)

# Store RGB values of all pixels in lists r, g and b
for row in batman_image:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

