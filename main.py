
a = [4,5,6,78]


def square2(a):
    return a ** 2

b = [square2(elm)/elm for elm in a]

print(b)






