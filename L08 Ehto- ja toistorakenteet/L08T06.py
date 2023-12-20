vuosi = int(input("Insert year: "))
if vuosi % 100 == 0 and vuosi % 400 != 0:
    print("Is not leap year!")
elif vuosi % 4 != 0:
    print("Is not leap year!")
else:
    print("Is leap year!")
