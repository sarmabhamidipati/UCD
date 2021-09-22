"""
PCA doesn't learn parts

Instructions
100 XP

    Import PCA from sklearn.decomposition.
    Create a PCA instance called model with 7 components.
    Apply the .fit_transform() method of model to samples. Assign the result to features.
    To each component of the model (accessed via model.components_), apply the show_as_image()
    function to that component inside the loop.

"""

# Import pyplot
from matplotlib import pyplot as plt
import numpy as np
from sklearn.decomposition import NMF
# Import PCA
from sklearn.decomposition import PCA

# using only test data here.
samples = np.array([[0., 0.], [0., 0.]])

print(samples.ndim)


def show_as_image(sample):
    bitmap = sample.reshape((-1, 1))
    plt.figure()
    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()


# Create an NMF model: model
model = NMF(n_components=1)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Create a PCA instance: model
model = PCA(n_components=1)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)
