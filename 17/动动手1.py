def sum(x):
    a = 0
    
    for each in x:
        if (type(each) == int) or (type(each) == float):
            a+=each
        else:
            continue
    return a
print(sum([1, 2.1, 2.3, 'a', '1', True]))
