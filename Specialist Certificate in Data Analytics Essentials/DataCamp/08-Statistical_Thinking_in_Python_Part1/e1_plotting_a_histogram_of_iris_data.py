"""

    Import matplotlib.pyplot and seaborn as their usual aliases (plt and sns).
    Use seaborn to set the plotting defaults.
    Plot a histogram of the Iris versicolor petal lengths using plt.hist()
    and the provided NumPy array versicolor_petal_length.
    Show the histogram using plt.show().

"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

versicolor_petal_length = np.array([4.7, 4.5, 4.9, 4., 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4.,
                                    4.7, 3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4., 4.9, 4.7, 4.3, 4.4,
                                    4.8, 5., 4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1,
                                    4., 4.4, 4.6, 4., 3.3, 4.2, 4.2, 4.2, 4.3, 3., 4.1])
print(versicolor_petal_length)

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Show histogram
plt.show()
