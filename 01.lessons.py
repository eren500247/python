def exponent(base,exp):
    num = exp
    a = 1
    while num > 0:
        a *= base
        num -= 1
    print(f"{base} exponent value is : {a}")
exponent(5,4)
    