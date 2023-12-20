def time(sec):
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    time = "%02d:%02d:%02d" % (hour, min, sec)
    return time
n = 112345
print(time(n))
