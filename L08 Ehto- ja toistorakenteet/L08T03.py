def check_int(num):
    #kirjoita koodisi tähän väliin
    if num == 10 or num == 20:
        retval = "Luku on 10 tai 20"
    elif num == 100 or num == 200:
        retval = "Luku on 100 tai 200"
    else:
        retval = num
    return retval