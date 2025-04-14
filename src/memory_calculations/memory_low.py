import numpy as np

def memory_low(x=1000, y=1000):
    matrix = np.random.rand(x, y)
    np.dot(matrix, matrix)


if __name__=='__main__':
    memory_low()
