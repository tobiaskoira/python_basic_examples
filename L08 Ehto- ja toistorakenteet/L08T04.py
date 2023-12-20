point = int(input("Insert your points: "))
if point >= 0 and point < 2:
    grade = 0
elif point >=2 and point < 4:
    grade = 1
elif point >=4 and point < 6:
    grade = 2
elif point >=6 and point < 8:
    grade = 3
elif point >=8 and point < 10:
    grade = 4
elif point >=10 and point <=12:
    grade = 5
print("Grade:", grade)


