it = "Wortspiel"

#W: 0
#o: 1
#r: 2
#t: 3
#s: 4
#p: 5
#i: 6
#e: 7
#l: 8

n = 2 #gib mir jedes zweite Element zurück

def nth_elements(it, n):
    for i, w in enumerate(it):
        if i % n == 0:
            yield i, w

result = list(nth_elements(it, n))
nums = [i[0] for i in result]
words = [i[1] for i in result]


for i in zip(nums,words):
    print(i)