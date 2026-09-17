import math 

def binary_cross_entropy(y_true, y_prob):
    result = [] 
    if len(y_true) != len(y_prob):
        raise ValueError("size")
    for label, prob in zip(y_true, y_prob):
        entropy = label * math.log(prob) + (1 - label) * math.log((1 - prob))
        result.append(entropy)

    return sum(result) / -len(y_true)

if __name__ == "__main__":
    print(binary_cross_entropy([1,0], [0.9, 0.2]))

