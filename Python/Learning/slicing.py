eingabe = "Titanic"
length = (len(eingabe))

print("----------------\n")

for i in range(length):
    print(eingabe[i]  + " : " + str(i) + " :  " + str(0-(length-i)))

print("----------------\n")

method1 = eingabe[6]
method2 = eingabe[-1]
method3 = eingabe[6:]

print(f'{method1} {method2} {method3}')