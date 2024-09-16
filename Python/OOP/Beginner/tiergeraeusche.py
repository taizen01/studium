import keyboard
number = []

while True:
    key = keyboard.press_and_release('1')
    if key == True:
        number.append(1)
        number_str = ''.join(map(str, number))
        print(number_str)
