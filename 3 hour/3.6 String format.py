# str.format() = optional method that gives users
#                more control when displaying output

# animal = "cow"
# item = "moon"
#
# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal,item))
# print("The {animal} jumped over the {item}".format(animal="dog", item="table"))

# name = "Albert"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:7}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) # this is by default
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))
