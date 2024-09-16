def weihnachtsbaum():
    size = int(input("Bitte gebe die größe des Baumes an: "))
    stern = input("Was möchtest du als Stern dekorieren? ")
    stamm = int(input("Wie viele stämme soll der baum haben "))
    stammsize = int(input("Wie lang soll soll der Stamm sein? "))

    i = 0
    k = size


    for run in range(stamm):
        while i <= size:
            j = "!"
            baum = 2*(i * j)+j
            space = " "
            baumstar = stern
            baumspace = (k * space)
            if i >= 1:
                print(baumspace + baum)
            else:
                print(baumspace + baumstar)
            k-=1
            i+=1
        i = 1
        k = size-1

    for i in range(stammsize):
        stammspace = (size * " ")
        print(stammspace + "H")


weihnachtsbaum()

