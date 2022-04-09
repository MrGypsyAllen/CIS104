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
#print(dct.items())
lst = list()
for k,v in dct.items() :
    newtup = (v,k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for v,k in lst[:1]:
    print(k,v)
