age = input("What is your age: ")
age = int(age)

if age >= 18:
    print("You are an adult")
    if age >= 30:
        if age>=40:
            print("I think you already have sons")
        else:
            print("You should think in having sons")
    else:
        print("You are at the best age")
        if age == 25:
            print("You are exactly twenty-five years old")
        elif age == 29:
            print("You are about to get thirty years old")
        else:
            print("You aren't 25 nor 29 years old")
    print("Hi, I'm always here greater than or equal to 18!")
else:
    print("You are still a very young")
temperature = int(input("What is the temperature today: "))

if temperature >=18 and temperature <=25:
    print("Go outside")
else:
    print("Stay inside")