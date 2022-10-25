name = "Bro"  # global scope (available inside and outside functions)


def display_name():
    name = "Code"  # local scope (available only inside this function)
    print(name)


display_name()
print(name)

# This behavior is called "LEGB" that means  Local, Enclosing, Global and  Built-in
