import numpy as np 
import time
import gc

def memory_medium():
    gc.disable()  # Disable garbage collection to prevent it from interfering with memory usage
    
    matrix = np.ones((6000, 3400))

    for _ in range(10):
        _ = matrix[::75]  # Read more rows to simulate more memory activity
        # time.sleep(0.5)

if __name__=='__main__':
    memory_medium()