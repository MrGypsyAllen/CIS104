Max = 0
Min = 100
while True :
    stringnum = input('Enter a number: ')

    if stringnum == 'done':
        break
    try:
        intnum = int(stringnum)
    except:
        print ('Invalid Input')
        continue
    if Max < intnum :
        Max = intnum
    elif Min > intnum :
        Min = intnum
    else:
        continue
print('Maximum is ', Max)
print('Minimum is ', Min)
