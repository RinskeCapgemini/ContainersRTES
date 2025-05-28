import numpy as np

"""High memory usage script."""

def memory_long():

    # Allocate a large matrix in memory and repeatedly access its elements.
    
    matrix = np.ones((11000, 5200))  # 450 MB = 11000 x 5200 x 8 bytes (by default float64)

    for i in range(10):
        temp = matrix[::25]  # Touch memory more frequently

if __name__=='__main__':
    memory_long()

