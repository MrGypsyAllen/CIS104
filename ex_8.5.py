#Curtis G Ex_7.2 CIS104
count = 0
try :
    help = input('Enter File Name: ')
    please = open(help)
    #print(please)
except :
    print('File Not Found!')
    quit()
for blip in please :
    blip = blip.rstrip()
    if blip.startswith('From:'):
        omg = blip.split()
        print(omg[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
