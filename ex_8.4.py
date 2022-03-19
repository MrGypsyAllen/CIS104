george = input('Enter file name: ')
file = open(george)
order = list()
for line in file :
    words = line.split()
    for word in words :
        if word in order :
            continue
        order.append(word)
order.sort()
print(order)
