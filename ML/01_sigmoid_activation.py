import math
def sigmoid(xs):
    return [1 / (1 + sum(math.exp(-x) for x in xs))]

if __name__ == "__main__":
    print(f"sigmoid = {sigmoid([-1,0,1])}")
