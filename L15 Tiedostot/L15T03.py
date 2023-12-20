filename = "nimet.txt"
file = open(filename, "r")
data = file.read()
words = data.split()
answer = sorted(words)
print(answer)
name = input("Anna etunimi: ")
if name in words:
        print("ok")
print('Number of words in text file :', len(words))
print('This name is',words.count(name), 'times in the text file')

file.close()