goku = dict()
try :
    vegeta = input('Enter file name: ')
    namek = open(vegeta)
except :
    print('No File Found!')
    quit()
for line in namek :
    words = line.split()
    if line.startswith('From ') :
        date = words[2]
        #print(words[2])
        goku[date] = goku.get(date, 0) + 1
print(goku.items())
