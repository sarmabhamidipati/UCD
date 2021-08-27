"""
The np.random module and Bernoulli trials
Define a function with signature perform_bernoulli_trials(n, p).

    Initialize to zero a variable n_success the counter of Trues, which are Bernoulli trial successes.
    Write a for loop where you perform a Bernoulli trial in each iteration and increment the number of success
    if the result is True. Perform n iterations by looping over range(n).
        To perform a Bernoulli trial, choose a random number between zero and one using np.random.random().
        If the number you chose is less than p, increment n_success (use the += 1 operator to achieve this).
    The function returns the number of successes n_success.
"""

import numpy as np
def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()
        if random_number < p:
            n_success += 1

        # If less than p, it's a success so add one to n_success
        if n < p:
            n_success += 1

    return n_success
