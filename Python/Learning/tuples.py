
starting_tuple = ("Yoda", "Han Solo", "R2D2", "C3PO") #Das ist ein Tupel

### Ein Tupel ist ein immutable Objekt, heißt Werte im Tupel können nicht mehr verändert werden
### Wie kann man jedoch das Tupel trotzdem noch ändern?

print(type(starting_tuple))

starting_tuple = list(starting_tuple)

starting_tuple.append("Darth Vader")

print(type(starting_tuple)) #starting_tuple ist nun ein mutable Objekt, heißt es können nun Werte verändert werden
print(starting_tuple)

starting_tuple = tuple(starting_tuple)

print(type(starting_tuple)) #starting_tuple ist nun wjeder ein immutable Objekt
print(starting_tuple)