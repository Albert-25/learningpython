# Dictionary = a changeable, unordered collection of unique key:value pairs

capitals = {
    "USA": "Washington DC",
    "India": "New Dehli",
    "China": "Beijing",
    "Russia": "Moscow"
}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "California"})
capitals.pop("China")
# capitals.clear()

print(capitals)
# print(capitals.get("India"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)
