import numpy as np
import time

"""Low memory usage script."""

def memory_low():

    # Allocate a smaller matrix in memory and acces elements.
    matrix = np.ones((4000, 3200)) 

    for i in range(10):
        temp = matrix[::100]  # Read memory to keep it active

if __name__=='__main__':
    memory_low()
