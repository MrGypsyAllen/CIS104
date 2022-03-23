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
largestvalue = -1
largekey = None
for key,value in dct.items() :
    if largestvalue < value :
        largestvalue = value
        largekey = key
print('Most messages sent:', largekey, largestvalue)
