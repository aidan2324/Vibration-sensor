import machine
from machine import Pin, ADC 
import utime 
 
#Initialize Prepherials
POT_Value = ADC(28) 
conversion_factor = 3.3/(65536)

#initialize last 1/10th of a second val

count = 0
last20 = []
for i in range(20):
        last20.append(POT_Value.read_u16() * conversion_factor)
        utime.sleep(0.01)

#Main Application loop
while True:
    curr = POT_Value.read_u16() * conversion_factor
    avg = sum(last20)/20
    last20.pop()
    last20.append(POT_Value.read_u16() * conversion_factor)
    if curr > avg * 1.5:
        count = count + 1
        print("Number:",  count, "VOLTAGE SPIKE.  AVG:", avg, "CURR", curr, "difference:", curr-avg, "Percent Diff:", (curr-avg)/avg*100)
        next20 = []
        for i in range(20):
            next20.append(POT_Value.read_u16() * conversion_factor)
            utime.sleep(0.01)
        print(last20[-5:], next20[0:5])
        for i in range(40):
            last20.pop()
            last20.append(POT_Value.read_u16() * conversion_factor)
            utime.sleep(0.01)
