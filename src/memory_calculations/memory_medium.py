import numpy as np 

def memory_medium(x=3000, y=3000):
    matrix = np.random.rand(x, y)
    np.dot(matrix, matrix)

if __name__=='__main__':
    memory_medium()