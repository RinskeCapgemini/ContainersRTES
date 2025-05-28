import numpy as np 

"""Medium memory usage script."""

def memory_medium():

    # Allocate a large matrix in memory and repeatedly access its elements.
    matrix = np.ones((6000, 3400))

    for _ in range(10):
        _ = matrix[::50]  # Read more rows to simulate more memory activity --> Was 75 for original experiments

if __name__=='__main__':
    memory_medium()