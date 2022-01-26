grade = input ('Please Enter Score: ')
try :
    score = float(grade)
except :
    print ('Bad Score')
    quit()
if score < 0.0 :
    print ('Bad Score')
elif score > 1.0 :
    print ('Bad Score')
elif score >= 0.9 :
    print ('Grade A')
elif score >= 0.8 :
    print ('Grade B')
elif score >= 0.7 :
    print ('Grade C')
elif score >= 0.6 :
    print ('Grade D')
elif score < 0.6 :
    print ('Grade F')
