words = "I tried so hard and got so far"

x = [x for x in words.split() if len(x) < 4]
