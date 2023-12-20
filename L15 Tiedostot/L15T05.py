import random

def lotto():
    nums = []
    for x in range(40):
        nums.append(False)
    i=0
    while i < 7:
        a=random.randrange(0,40)  
        if not nums[a]:
            nums[a]=True
            i+=1
    txt=""
    
    for x in nums:
        i +=1
        if x:
            txt += str(i)+','+ ' '
    numbers = txt.strip(', ')
    return numbers
result = lotto()

print(result)
filename = "lotto.txt"
file = open (filename, "w")
msg = str(result)
file.write(msg)
file.close()