# *args = parameter  that will pack all arguments into a tuple useful so that
#         a function  can accept a varying amount of arguments

def hello(*args):
    for i in args:
        if args[len(args) - 1] == i:
            print(i)
        else:
            print(i, end="")


hello("h", "o", "l", "a", "!!")


def add(*stuff):
    sum = 0
    stuff = list(stuff)  # with the list method it is possible change the nature of a tuple into a list
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


print(add(1, 2, 3))


def prueba(*args):
    print(args[0])
    print(args[1])


prueba(1, 2)
