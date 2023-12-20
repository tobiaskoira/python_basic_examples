try:
    numbers=[1,2,3,4,5]
    numbers[5] = "6"
    print("Listan pituus on", len(numbers))
except IndexError:
    print("Listalla ei ole noin montaa elementtiä")

