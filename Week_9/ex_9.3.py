dct = dict()
try :
    fhand = input('Enter file name: ')
    namek = open(fhand)
except :
    print('No File Found!')
    quit()
for line in namek :
    words = line.split()
    if line.startswith('From ') :
        date = words[1]
        #print(words[2])
        dct[date] = dct.get(date, 0) + 1
print(dct.items())
