"""
Run_n_times()

Add the run_n_times() decorator to print_sum() using decorator syntax so that print_sum() runs 10 times.
Use run_n_times() to create a decorator run_five_times() that will run any function five times.
Here's the prank: use run_n_times() to modify the built-in print() function so that it always prints 20 times!
"""


def run_n_times(n):
    """Define and return a decorator"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
    print(a + b)


print_sum(15, 20)

# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)


@run_five_times
def print_sum(a, b):
    print(a + b)


print_sum(4, 100)

# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')