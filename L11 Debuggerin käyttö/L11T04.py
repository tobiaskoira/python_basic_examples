point1= int(input('Give points:'))
point2= int(input('Give points:'))
point3= int(input('Give points:'))
point4= int(input('Give points:'))
point5= int(input('Give points:'))
points = [point1, point2, point3, point4, point5]
max = max(points)
min = min(points)
summa = sum([point1, point2, point3, point4, point5]) - max - min
print('Total points are:',summa)


