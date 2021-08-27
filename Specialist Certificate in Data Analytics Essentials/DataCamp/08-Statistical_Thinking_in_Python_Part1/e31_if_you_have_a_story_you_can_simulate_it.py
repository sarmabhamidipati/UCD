"""
If you have a story, you can simulate it!
Define a function with call signature successive_poisson(tau1, tau2, size=1) that samples the waiting time
for a no-hitter and a hit of the cycle.

    Draw waiting times tau1 (size number of samples) for the no-hitter out of an exponential distribution
    and assign to t1.
    Draw waiting times tau2 (size number of samples) for hitting the cycle out of an exponential distribution
    and assign to t2.
    The function returns the sum of the waiting times for the two events.
"""
import numpy as np
def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2