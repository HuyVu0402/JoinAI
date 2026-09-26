def median(values):
    n = len(values)
    values = sorted(values)
    if n % 2 == 0:
        return (values[n // 2 - 1]+ values[n//2]) / 2
    else:
        return values[n//2]
print(median([8,1,10,3]))
