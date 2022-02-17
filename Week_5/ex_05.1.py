count = 0
total = 0.0
while True :
    stringnum = input('Enter a number: ')
    if stringnum == 'done':
        break
    try:
        floatnum = float(stringnum)
    except:
        print ('Invalid Input')
        continue
    count = count + 1
    total = total + floatnum
print (total, count, total/count)
