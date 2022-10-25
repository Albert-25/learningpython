# set = collection which  is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("new_element")
utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
dishes_table = utensils.union(dishes)  # this union method allows mix two sets and get an only set

print(dishes.difference(utensils))
print(utensils.intersection(dishes))

print("==============¨¨=============")

for i in dishes_table:
    print(i)
