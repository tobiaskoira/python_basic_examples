def celToFah(cel):
    fah = (9 / 5.0 * cel) + 32
    return round(fah,1)

def fahToCel(fah):
    cel = 5.0*(fah - 32) / 9
    return round(cel, 1)

