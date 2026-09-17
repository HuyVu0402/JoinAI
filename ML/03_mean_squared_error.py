def mse(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("not the same length y_true and y_pred")

    n = len(y_true)

    squared_error = sum((i - j) ** 2 for i,j in zip(y_true, y_pred))

    return squared_error / n

if __name__ == "__main__":
    y_true = list(map(float, input("input your true label: ").split()))
    y_pred = list(map(float, input("input your prediction label: ").split()))
    print(mse(y_true, y_pred))
