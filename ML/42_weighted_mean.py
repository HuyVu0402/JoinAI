def weighted_mean(values, weights):
    return sum(i*j for i,j in zip(values,weights)) / sum(i for i in weights)

print(weighted_mean([10,20],[1,3]))
