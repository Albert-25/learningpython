food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[4] = "Ceviche"

food.append("Ají de gallina")
food.remove("spaghetti")
food.pop()
food.insert(1, "I'm at the index one")
food.insert(2, "I'm at the index two")
food.sort()
food.clear()  # this line remove all the items from the list ( [] )

for i in food:
    print(i)

print(food)
