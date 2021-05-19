def huiwen(x):
    y = str(x)[::-1]
    if y == str(x):
        return True
    else:
        return False
    

print(huiwen(191))