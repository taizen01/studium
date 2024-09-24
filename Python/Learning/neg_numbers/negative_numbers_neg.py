import time
import os
from bit_operations import bin_convert, bit_length, twos_complement_to_decimal

os.system('cls')

GRUEN = "\033[92m"
GELB = "\033[33m"
RESET = "\033[0m"


ganzahl = int(input("Bitte gib eine positive Ganzzahl ein: ")) 
if ganzahl > 0:
    print("----------------------------------------------------------")
else:
    print("Zahl war nicht positiv") 
    exit()

print(GELB +"\nAls Dezimalzahl: " + str(ganzahl) + "\n")
print("In Bitdarstellung: " + bit_length(ganzahl) + "\n" + RESET)
print("----------------------------------------------------------\n")
time.sleep(1)
print("Negiere alle Bits...\n")
time.sleep(1)


print("Bits der Ganzahl negiert: " + bin_convert(bit_length(ganzahl)) + "\n")
time.sleep(1)

result = bin(int(bin_convert(bit_length(ganzahl)),2) +1)

print("Addiere Binär 1 auf die negierte Binärzahl ...\n")

print("----------------------------------------------------------\n")
print(GRUEN + "In Bitdarstellung: " + str(result[2:]) + "\n")
print("Dezimalzahl der Umwandlung: " + str(twos_complement_to_decimal(str(result[2:]))) + RESET + "\n")
    
print("Länge der Bits der Binärzahl: " + str(len(str(result[2:]))) + "bits\n")
print("----------------------------------------------------------")