def edit_distance(a, b):
    char_a = list(a)
    char_b = list(b)
    row = len(char_a) + 1
    col = len(char_b) + 1
    result = 0

    for i in range(row):
        l = []


