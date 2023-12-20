nimi = "x"
i = 0
nimet = ''
list = [nimet]
while nimi != "":
    nimi = str(input("Enter student name:"))
    
    if nimi != "":
        i = i + 1
        nimet = nimet + str(nimi)+','+ ' '
        
    else:
        print("Student count:", i)
        print(nimet.strip(', ') )
