import math 

def softmax(logits):
    max_value = max(logits)
    result = [] 
    total = sum(math.exp(i - max_value) for i in logits)
    for i in range(len(logits)):
        softmax_i = math.exp(logits[i] - max_value) / total
        result.append(softmax_i)
    return result

if __name__ == "__main__":
    x = list(map(float, input("nhập mảng: ").split()))
    print(softmax(x))
