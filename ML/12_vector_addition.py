import numpy as np 
def vector_add(a, b):
    a_np = np.array(a)
    b_np = np.array(b)
    return a_np + b_np

if __name__ == "__main__":
    a = [1,2]
    b = [3,4]
    print(vector_add(a,b))
