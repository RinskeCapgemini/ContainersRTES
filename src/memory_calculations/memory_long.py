import numpy as np
import time

def memory_long():
    # ~450 MB = 11000 x 5200 x 8 bytes
    matrix = np.ones((11000, 5200))

    for _ in range(10):
        _ = matrix[::25]  # Touch memory more frequently
        time.sleep(0.5)

if __name__=='__main__':
    memory_long()

