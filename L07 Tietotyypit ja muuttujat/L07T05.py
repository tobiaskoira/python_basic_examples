balance = 2000
print("Bank account balance:", balance, "€")
summaEuro = input("How many euros will be added to the balance? ")
summaCents = input("How many cents will be added to the balance? ")
summaTotal = int(balance) + int(summaEuro) + int(summaCents)*0.01
print("Bank account balance:", summaTotal, "€")