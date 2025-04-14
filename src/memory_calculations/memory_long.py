import numpy as np

def memory_long(x=5000, y=5000):
    matrix = np.random.rand(x, y)
    np.dot(matrix, matrix)

if __name__=='__main__':
    memory_long()

