import numpy as np 

def top_k(scores, k):
    scores = np.array(scores)
    return np.argsort(-scores)[:k]

if __name__ == "__main__":
    print(top_k([0.2, 0.9, 0.5], 2))
