Hours = input ("Enter Hours: ")
Rate = input ("Enter Rate: ")
try :
    Fhours = float(Hours)
    Frate = float(Rate)
except:
    print ("Error, Enter a numeric input.")
    quit()
if Fhours <= 40 :
    Pay = Fhours * Frate
else :
    Reg = Fhours * Frate
    OtPay = (Fhours - 40) * (Frate * 1.5)
    Pay = Reg + OtPay
print ("Pay:" ,Pay)
