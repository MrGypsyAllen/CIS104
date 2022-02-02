#Curtis G ex_4.0
#import time
def newmax(a, b, c) :
    if (a > b) and (a > c) :
        print(a)
    elif (b > a) and (b > c) :
        print(b)
    else :
        print(c)

newmax(1, 2, 3)
newmax(3, 2, 1)
newmax(10, 65, 23)
#time.sleep(5.0)
