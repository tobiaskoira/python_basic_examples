class Cat:
    def __init__(self, name="", color=""):
        self.name=name
        self.color=color

    def __str__(self):
        return self.name + " " + self.color

    name = ""
    color = ""
    def miau(self):
        return self.name + " " + "says: Meoooooow!"


cat1=Cat("Kit","black")
cat2=Cat("Kat", "white")

print(cat1.name + ", " + "color: " + cat1.color)
print(cat2.name + ", " + "color: " + cat2.color)
print(cat1.miau())
print(cat2.miau())