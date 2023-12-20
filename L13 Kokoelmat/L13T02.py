try:
    luku = "x"
    i = 0
    summa = 0
    list=[]

    while luku != "":
        luku = int(input("Anna luku: "))
        
        
        if luku <=5 and luku >=0:
            list.append(luku)
            i = i + 1
            summa=summa+int(luku)
            keskiarvo = int(summa/i)

                     
        else:
            print("Anna kokonaisuluku 0,1,2,3,4 tai 5")

except:

    print("Lukujen keskiarvo:", keskiarvo) 
    print("Lukuja annettu:", len(list))

