#Curtis G Ex_7.2 CIS104
count = 0
total = 0
try :
    help = input('Enter File Name: ')
    please = open(help)
    #print(please)
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
        #print(total)

print('Average spam confidence: ',average)
#print(blip)
