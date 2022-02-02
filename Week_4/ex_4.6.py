def computepay(hours, rate):
    print ('Computepay', hours, rate)
    if Fhours <= 40 :
        pay = Fhours * Frate
    else :
        Reg = Fhours * Frate
        OtPay = (Fhours - 40) * (Frate * .5)
        pay = Reg + OtPay
    return(pay)
hours = input ("Enter Hours: ")
rate = input ("Enter Rate: ")
Fhours = float(hours)
Frate = float(rate)

pay = computepay(Fhours, Frate)
print ("Pay:" ,pay)
