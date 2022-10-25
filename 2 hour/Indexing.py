# index operator [] = gives access to a sequence's element(str, lists, tuples)

name = "bro Code!"

print(name[0].islower())

# if name[0].islower():
#     name = name.capitalize()
#
# print(name)

sub_string1 = name[:3].upper()
print(sub_string1)
sub_string2 = name[4:]
print(sub_string2)
sub_string2 = name[4:].lower()
print(sub_string2)
last_character = name[-1]
print(last_character)
