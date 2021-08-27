"""
The standard deviation and the variance


    Compute the variance of the data in the versicolor_petal_length array using np.var()
    and store it in a variable called variance.

    Print the square root of this value.

    Print the standard deviation of the data in the versicolor_petal_length array using np.std().

"""
import numpy as np

versicolor_petal_length = np.array([4.7, 4.5, 4.9, 4., 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4.,
                                    4.7, 3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4., 4.9, 4.7, 4.3, 4.4,
                                    4.8, 5., 4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1,
                                    4., 4.4, 4.6, 4., 3.3, 4.2, 4.2, 4.2, 4.3, 3., 4.1])

# Array of differences to mean: differences

differences = versicolor_petal_length - np.mean(versicolor_petal_length)
# Square the differences: diff_sq
diff_sq = differences ** 2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np

variance_np = np.var(versicolor_petal_length)

# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))
