afile = open('mbox-short.txt')

for line in afile :
    line1 = line.rstrip()
    print(line1.upper())
