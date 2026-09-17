def min_max_normalize(xs):
    min_value = min(xs)
    max_value = max(xs)
    
    if min_value == max_value:
        return [0.0 for _ in xs]

    range_val = max_value - min_value 
    return [(value - min_value) / range_val for value in xs]

if __name__ == "__main__":
    print(min_max_normalize(list(map(int,input().split()))))
