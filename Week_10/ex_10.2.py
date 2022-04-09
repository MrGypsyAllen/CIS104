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
        hour = words[5]
        getit = hour.split(':')
        ope = getit[0]
        #print(ope)
        dct[ope] = dct.get(ope, 0) + 1

#print(dct.items())

jk = (sorted([(k,v) for k,v in dct.items()]))
for k,v in jk :
    print(k,v)
