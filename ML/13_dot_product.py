def dot_product(a, b):
    return sum(i * j for i,j in zip(a,b))

if __name__ == "__name__":
    print(dot_product([1,1], [1,1]))

