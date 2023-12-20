class Car:
    def __init__(self, brand="", model="", price=""):
        self.brand=brand
        self.model=model
        self.price=price

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)

    brand = ""
    model = ""
    price = 0

car1=Car("Skoda","Octavia", 3000)
car2=Car("Audi","A4", 4000)
car3=Car("Volvo","V70", 5000)

summa = car1.price + car2.price + car3.price

print("car1:", car1)
print("car2:", car2)
print("car3:", car3)
print("Total price of the cars is",summa)

