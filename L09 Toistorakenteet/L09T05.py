def lotto():
    import random
    string = []
    for number in range (0, 7):
        string.append(str(random.randint(1,40)))
    return ','.join(string)
