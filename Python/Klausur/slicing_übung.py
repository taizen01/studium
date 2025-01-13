# von -> inklusive
# bis -> exklusive
# syntax slicing string[<von>:<bis>:<schrittweite, default=1>]

word = "Superman"

#S: 0 -8
#u: 1 -7
#p: 2 -6
#e: 3 -5
#r: 4 -4
#m: 5 -3
#a: 6 -2
#n: 7 -1

#Rückwärts ausgabe
print(word[::-1]) #sollte "nam" rauskommen 

#Vorwärts ausgabe
print(word[::1])

#jeden zweiten buchstaben
print(word[::2])

#Rückwärts jeden zweiten Buchstaben
print(word[-1:-9:-2])

