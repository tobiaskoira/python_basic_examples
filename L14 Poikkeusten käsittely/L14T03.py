def isthiszero(num):
    number = int(num)
    if number == 0:
        return True
    else:
        return False
try:
    num = 0
    isthiszero(num)
    print("number is", num)
except TypeError:
    print("Typeerror")

