def one_hot(indices, num_classes):
    result = []
    for label in indices:
        one_hot = [0] * num_classes
        one_hot[label] = 1
        # print(f"label = {label}, {result}")
        result.append(one_hot)
        # print(f"after add one hot: {resulit}")
    return result 

if __name__ == "__main__":
    print(one_hot([0,2,1],3))
