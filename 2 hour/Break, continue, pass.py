while True:
    name = input("What is your name:")
    if name !="":
        break

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 11):
    if i == 5:
        pass
    else:
        print(i)
