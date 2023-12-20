age = int(input("kerro ikä: "))
if age < 13:
    print("child")
elif age >= 13 and age < 20:
    print("teen")
elif age >= 20 and age <= 65:
    print("adult")
else:
    print("senior")