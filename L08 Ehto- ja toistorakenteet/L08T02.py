integer1 = input("Input integer: ")
integer2 = input("Input another integer: ")
integer3 = input("One more: ")
if integer1 > integer2 and integer1 > integer3:
    tulos = integer1
elif integer2 > integer1 and integer2 > integer3:    
    tulos = integer2
elif integer3 > integer1 and integer3 > integer2:
    tulos = integer3
print("Max value:", tulos)