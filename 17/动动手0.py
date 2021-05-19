def min(x):
    a = x[0]

    for each in x:
        if each < a:
            a = each
    return a

print(min('578952014257'))