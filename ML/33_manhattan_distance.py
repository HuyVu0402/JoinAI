def manhattan_distance(a, b):
    return sum(abs(a_i - b_i) for a_i, b_i in zip(a,b))

if __name__ == "__main__":
    print(manhattan_distance([1,1], [4,3]))
