import string
dct = dict()
lst = list()
count = 0
try :
    fhand = input('Enter file name: ')
    file = open(fhand)
except :
    print('No File Found!')
    quit()

for line in file :
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
            count += 1
            if letter not in dct :
                dct[letter] = 1
            else :
                dct[letter] += 1

for key, val in list(dct.items()) :
    lst.append((count / val , key))

lst.sort(reverse=True)

for key, val in lst :
    print(int(key), val)
