def mae(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("error length")
    length = len(y_true)
    abs_error = sum(abs(y - y_exp) for y,y_exp in zip(y_true, y_pred))
    return abs_error / length

if __name__ == "__main__":
    print(mae([1,2,3], [1,4,2]))
