def purify(x):
    result = []
    for num in x:
        if num % 2 == 0:
            result.append(num)
    return result