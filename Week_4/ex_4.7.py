def computegrade(grade) :
    #print('Your Grade: ',grade)
    if score < 0.0 :
        return ('Bad Score')
    elif score > 1.0 :
        return ('Bad Score')
    elif score >= 0.9 :
        return ('A')
    elif score >= 0.8 :
        return ('B')
    elif score >= 0.7 :
        return ('C')
    elif score >= 0.6 :
        return ('D')
    else :
        return ('F')
grade = input ('Please Enter Score: ')
try :
    score = float(grade)
except :
    print ('Bad Score')
    quit()
print (computegrade(score))
