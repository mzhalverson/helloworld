def collatz(z):
    if z == 1:
        print("All done!!!")
    elif z%2 == 0:
        print(z/2)
        collatz(z/2)
    else:
        print(3*z+1)
        collatz(3*z+1)
# print(collatz(42))


def collatzHopes(z):
    i = 0
    while z != 1:
        if z%2 == 0:
            z = z/2
        else:
            z = 3*z+1
        i=i+1
    return True, i
print(collatzHopes(4))