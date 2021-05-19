def people(n,one):
    if n-1:
        one += 2
        n -= 1
        return people(n,one)
    else:
        return one

print(people(5,10))