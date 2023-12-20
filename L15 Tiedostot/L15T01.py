filename = "names.txt"
file = open(filename, "w")
surname = input("Give a surname: ")
file.write(surname + "\n")
file.close()
