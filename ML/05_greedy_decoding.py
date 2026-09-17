def greedy_decode(logits):
    result = []
    for i in range(len(logits)):
        ind = logits[i].index(max(logits[i]))
        result.append(ind)
    return result

if __name__ == "__main__":
    logits = [[2,1,0],[0,5,1],[3,3,9]]
    print(greedy_decode(logits))
