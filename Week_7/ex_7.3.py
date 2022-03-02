#Curtis G Ex_7.3 CIS104
count = 0
total = 0

help = input('Enter File Name: ')
if help == 'na na boo boo' :
    print('NA NA BOO BOO to you too!')
    quit()

else:
    try :
        please = open(help)
    except :
        print('File Not Found!')
        quit()
    for blip in please :
        blip = blip.rstrip()
        if blip.startswith('X-DSPAM-Confidence:'):
            count = count + 1
            numbers = float(blip[20:])
            total = total + numbers
            average = total / count

print('Average spam confidence: ',average)
#print(blip)
