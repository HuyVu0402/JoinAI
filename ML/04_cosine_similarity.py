import math

def cosine_similarity(a, b):
    if len(a) != len(b):
        raise ValueError("Dim")
    dot_product = sum(i*j for i,j in zip(a,b))
    norm_a = math.sqrt(sum(i**2 for i in a))
    norm_b = math.sqrt(sum(j**2 for j in b))
    return dot_product / (norm_a * norm_b)

if __name__ == "__main__":
    a = list(map(float, input("input the first vector: ").split()))
    b = list(map(float, input("input the second vector: ").split()))
    print(cosine_similarity(a, b))
