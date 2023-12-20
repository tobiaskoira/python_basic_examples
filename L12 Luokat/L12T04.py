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
import random
CarBrand = ['Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo', 'VW']
car1=Car(random.choice(CarBrand),"", random.randint(1000, 10000))
car2=Car(random.choice(CarBrand),"", random.randint(1000, 10000))
car3=Car(random.choice(CarBrand),"", random.randint(1000, 10000))
car4=Car(random.choice(CarBrand),"", random.randint(1000, 10000))
car5=Car(random.choice(CarBrand),"", random.randint(1000, 10000))
cars=[car1, car2, car3, car4, car5]

