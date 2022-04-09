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
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    for numb in x :
        numb = int(numb)
        lst = lst + [numb]
#print(lst)
sum = sum(lst)
count = int(len(lst))
if count :
    aver = sum / count
print(int(aver))
