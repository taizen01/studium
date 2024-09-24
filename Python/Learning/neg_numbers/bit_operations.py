def bin_convert(input):
    binzärzahl = str(input)
    output = []

    for i in range(len(binzärzahl)):
        if binzärzahl[i] == "1":
            output.append("0")
        elif binzärzahl[i] == "-":
            output.append("-")
        elif binzärzahl[i] == "0":
            output.append("1")
        else:
            print("Das war keine Binärzahl verlasse das Programm ...")
            exit()

    result = "".join(output)
    return result


def bit_length(zahl):
    bit_width = zahl.bit_length()
    if bit_width == 0:
        bit_width = 8
    elif bit_width <= 8:
        bit_width = 8
    elif bit_width <= 16:
        bit_width = 16
    else:
        bit_width = ((bit_width+15)//16)*16
    return f'{zahl:0{bit_width}b}'



def twos_complement_to_decimal(binary_str):
    n = len(binary_str)  # Länge der binären Zahl
    # Prüfen, ob das erste Bit 1 ist (negative Zahl)
    if binary_str[0] == '1':
        # Berechne das Zweierkomplement, um den negativen Wert zu erhalten
        return int(binary_str, 2) - (1 << n)  # (1 << n) ist 2^n
    else:
        # Positive Zahl, einfach umwandeln
        return int(binary_str, 2)