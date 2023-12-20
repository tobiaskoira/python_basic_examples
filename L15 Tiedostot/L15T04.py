numbers=[]
while True:
    number = input ('Anna numero: ')
    if number  == '':
        break
    elif int(number) - float(number) == 0:
        result = numbers.append(number)
        filename = 'intnumbers.txt'
        file = open (filename, "w")
        msg = str(result)
        file.write(msg)
        file.close()

    else:
        result = numbers.append(number)
        filename = "floatnumbers.txt"
        file = open (filename, "w")
        msg = str(result)
        file.write(msg)
        file.close()
print('Anna luku: ')
