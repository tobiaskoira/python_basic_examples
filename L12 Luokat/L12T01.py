class Human:
    def __init__(self, name="", age=""):
        self.name=name
        self.age=age

    def __str__(self):
        return self.name + " " + str(self.age)

    name = ""
    age = 0

human1=Human("Adam",18)
human2=Human("Eva",18)

print(human1)
print(human2)
