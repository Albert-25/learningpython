# **kwargs is a parameter that will pack arguments into a dictionary
#           useful so  that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    print("hello " + kwargs["first"] + " " + kwargs["last"])

    for key, value in kwargs.items():
        print(key + ": ", value)
        # print(value, end=" ")


hello(first="Albert", last="Smith")
