def power2(b, e):
    if e == 0:
        return 1
    else:
        return b * power2(b, e-1)



print(power2(2,1))

def power_rec(base, exp, result=1):
    if exp == 0:
        return result
    else:
        return power_rec(base,exp-1,base*result)
    

print(power_rec(2,4))