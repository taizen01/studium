def myfunktion():
    n = 1
    while n <= 10:
        yield n
        n +=1

m = next(myfunktion())
v = next(myfunktion())

print(m)
print(v)