def scale_vector(v, c):
    return [c * value for value in v]

if __name__ == "__main__":
    print(scale_vector([1, -3], 2))
