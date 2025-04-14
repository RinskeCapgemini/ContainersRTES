import numpy as np 
import time

def memory_medium():
    matrix = np.ones((7000, 3600))

    for _ in range(10):
        _ = matrix[::50]  # Read more rows to simulate more memory activity
        # time.sleep(0.5)

if __name__=='__main__':
    memory_medium()