string = 'X-DSPAM-Confidence: 0.8475 '
start = string.find(':')
#print(start)
step1 = string[18+1:]
#step2 = step1.strip()
float = float(step1)
print(float)
#print(type(float))
