def l1_norm(x):
    return sum(abs(i) for i in x)

if __name__ == "__main__":
    print(l1_norm([-2,3]))
