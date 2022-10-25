name = "albert smith a"

print(len(name))
print(name.find("b")) # the index of the character
print(name.capitalize()) # only convert the first letter to capital
print(name.upper()) # convert all letters to capital
print(name.lower()) # convert all letters to lowercase
print(name.isdigit()) # name must be a string, true if it's number, false if it is not
print(name.isalpha()) # true if it's only letters
print(name.count("a")) # number of character
print(name.replace("a", "e")) # first is replaced by the second
print(name*2)