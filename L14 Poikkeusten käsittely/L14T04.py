try:
    list = ["apple", "orange", "melon", "ananas"]
    place = int(input("In which place you want to add a fruit "))
    newName = input("give a fruit name ")
    list[place]=newName
    print("List content is", list)
except IndexError:
    print("Where are no so much items, please try again")