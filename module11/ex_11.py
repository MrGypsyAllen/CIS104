import re
count = 0
lst = []
try:
    fname = input('Enter file name: ')
    fhand = open(fname)
except:
    print('File cannot be opened: ',fname)
    exit()

for line in fhand:
    line = line.rstrip()
    x = re.findall('\d+', line)
    for numb in x :
        numb = int(numb)
        lst = lst + [numb]
#print(lst)
sum = sum(lst)
print(sum)
