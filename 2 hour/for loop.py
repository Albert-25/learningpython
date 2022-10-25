import time

for i in range(10):
    print(i)

print("####################################")
for i in range(10, 20):
    print(i)

print("####################################")
for i in range(10, 20, 2):
    print(i)

name = "Albert Smith"

for i in name:
    print(i)

# mine
for i in range(len(name)):
    print("index " + str(i) + ": " + name[i])

# cool #
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Happy New Year!!")
# cool #

signal = "</> "

for i in range(1,6):
    print(signal*i)

for i in range(4,0,-1):
    print(signal*i)
