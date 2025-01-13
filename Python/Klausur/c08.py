alphabet = ["a","b","c","c","d","e","e"]

temp = set(alphabet)

alphabet = list(temp)
alphabet.sort()

if alphabet.__contains__("f"):
    ...
else:
    alphabet += ["f"]

a,b = alphabet[0], alphabet[1]

print(alphabet)

print(a)

print(b)