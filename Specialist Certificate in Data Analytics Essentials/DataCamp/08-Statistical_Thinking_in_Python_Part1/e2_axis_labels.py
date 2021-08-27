"""
Axis labels!
Label the axes. Don't forget that you should always include units in your axis labels.
Your -axis label is just 'count'. Your
-axis label is 'petal length (cm)'. The units are essential!
Display the plot constructed in the above steps using plt.show().
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

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')
# Show histogram
plt.show()

