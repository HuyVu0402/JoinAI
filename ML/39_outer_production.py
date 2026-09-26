def outer_product(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b)):
            row.append(a[i] * b[j])
        result.append(row)
    return result 

print(outer_product([1,2], [3,4]))
