import numpy as np
import time

def memory_low():
    matrix = np.ones((4000, 3200)) 

    for _ in range(10):
        _ = matrix[::100]  # Read some memory to keep it "active"
        time.sleep(0.5)


if __name__=='__main__':
    memory_low()
