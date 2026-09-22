import math 

def l2_norm(x):
    if len(x) == 0:
        return 0 
    sum_square = sum(i ** 2 for i in x)
    return math.sqrt(sum_square)

if __name__ == "__main__":
    print(l2_norm([3,4]))
