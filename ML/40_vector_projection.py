def project_vector(a, b):
    dot_production = sum(i*j for i, j in zip(a,b))
    square_b = sum(i**2 for i in b)
    return [i * dot_production / square_b for i in b]

print(project_vector([2,2], [1,0]))
