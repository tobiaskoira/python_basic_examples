matka = float(input("Enter trip length in km:"))
hinta = float(input("Enter fuel price/liter:"))
kulutus = float(input("Enter fuel consumption/100 km:"))
def calc_consumption():
    Fuel = (kulutus*matka)/100
    Cost =  Fuel * hinta
    print("Fuel:",'{:.2f}'.format(round(Fuel,2)),"liter")
    print("Cost:",'{:.2f}'.format(round(Cost,2)),"€")
calc_consumption()
