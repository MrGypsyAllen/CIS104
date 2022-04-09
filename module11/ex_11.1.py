import re

count = 0

input_exp = input('Enter a Reguler Expression: ')
reg_ex = str(input_exp)
fname ='mbox-short.txt'
fhand = open(fname)

for line in fhand :
    line = line.rstrip()

    if re.findall(reg_ex, line) != []:
        count = count + 1

print(fname + ' had ' + str(count) + ' line that matched ' + reg_ex)
