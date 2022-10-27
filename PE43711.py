from locale import ABMON_10
from re import A
import RPi.GPIO as GPIO
import time

# Declare the pin number
#PE44820
PIN_HIGH_P = 0
P_or_S = 26
OPT = 19
D0 = 22
D1 = 10
D2 = 9
D3 = 11
D4 = 0
D5 = 5
D6 = 6
D7 = 13
pins_P = [D0, D1, D2, D3, D4, D5, D6, D7]
#PE43711
PIN_HIGH_A = 0
A0 = 14
A1 = 15
A2 = 18
A3 = 23
A4 = 24
A5 = 25
A6 = 8
LE = 7
pins_P_A = [A0, A1, A2, A3, A4, A5, A6]
# Set GPIO mode
#라즈베리파이 핀 번호를 GPIO 번호로 사용
#GPIO.setmode(GPIO.BOARD)
#회로의 GPIO 번호 사용
GPIO.setmode(GPIO.BCM)

# Set GPIO Pin
GPIO.setup(P_or_S, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(OPT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LE, GPIO.OUT, initial=GPIO.HIGH)

for pin in pins_P:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
for pin in pins_P_A:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
time.sleep(2)
print("Initial setup complete")

# Controll Pin
GPIO.output(P_or_S, GPIO.LOW)
GPIO.output(OPT, GPIO.LOW)
while (True):
    PIN_HIGH_P = int(input("PIN Number of PS to set HIGH: "))
    PIN_HIGH_A = int(input("PIN Number of dB to set HIGH: "))
    
    if PIN_HIGH_P == 0:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH_P = 22
        
        if PIN_HIGH_A == 0:
            PIN_HIGH_A = 14
        elif PIN_HIGH_A == 1:
            PIN_HIGH_A = 15
        elif PIN_HIGH_A == 2:
            PIN_HIGH_A = 18
        elif PIN_HIGH_A == 3:
            PIN_HIGH_A = 23
        elif PIN_HIGH_A == 4:
            PIN_HIGH_A = 24
        elif PIN_HIGH_A == 5:
            PIN_HIGH_A = 25
        elif PIN_HIGH_A == 6:
            PIN_HIGH_A = 8
        
    elif PIN_HIGH_P == 1:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH_P = 10
        
        if PIN_HIGH_A == 0:
            PIN_HIGH_A = 14
        elif PIN_HIGH_A == 1:
            PIN_HIGH_A = 15
        elif PIN_HIGH_A == 2:
            PIN_HIGH_A = 18
        elif PIN_HIGH_A == 3:
            PIN_HIGH_A = 23
        elif PIN_HIGH_A == 4:
            PIN_HIGH_A = 24
        elif PIN_HIGH_A == 5:
            PIN_HIGH_A = 25
        elif PIN_HIGH_A == 6:
            PIN_HIGH_A = 8
        
    elif PIN_HIGH_P == 2:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH_P = 9
        
        if PIN_HIGH_A == 0:
            PIN_HIGH_A = 14
        elif PIN_HIGH_A == 1:
            PIN_HIGH_A = 15
        elif PIN_HIGH_A == 2:
            PIN_HIGH_A = 18
        elif PIN_HIGH_A == 3:
            PIN_HIGH_A = 23
        elif PIN_HIGH_A == 4:
            PIN_HIGH_A = 24
        elif PIN_HIGH_A == 5:
            PIN_HIGH_A = 25
        elif PIN_HIGH_A == 6:
            PIN_HIGH_A = 8
        
    elif PIN_HIGH_P == 3:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH_P = 11
        
        if PIN_HIGH_A == 0:
            PIN_HIGH_A = 14
        elif PIN_HIGH_A == 1:
            PIN_HIGH_A = 15
        elif PIN_HIGH_A == 2:
            PIN_HIGH_A = 18
        elif PIN_HIGH_A == 3:
            PIN_HIGH_A = 23
        elif PIN_HIGH_A == 4:
            PIN_HIGH_A = 24
        elif PIN_HIGH_A == 5:
            PIN_HIGH_A = 25
        elif PIN_HIGH_A == 6:
            PIN_HIGH_A = 8
        
    elif PIN_HIGH_P == 4:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH_P = 0       
        
        if PIN_HIGH_A == 0:
            PIN_HIGH_A = 14
        elif PIN_HIGH_A == 1:
            PIN_HIGH_A = 15
        elif PIN_HIGH_A == 2:
            PIN_HIGH_A = 18
        elif PIN_HIGH_A == 3:
            PIN_HIGH_A = 23
        elif PIN_HIGH_A == 4:
            PIN_HIGH_A = 24
        elif PIN_HIGH_A == 5:
            PIN_HIGH_A = 25
        elif PIN_HIGH_A == 6:
            PIN_HIGH_A = 8 
        
    elif PIN_HIGH_P == 5:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH_P = 5
        
        if PIN_HIGH_A == 0:
            PIN_HIGH_A = 14
        elif PIN_HIGH_A == 1:
            PIN_HIGH_A = 15
        elif PIN_HIGH_A == 2:
            PIN_HIGH_A = 18
        elif PIN_HIGH_A == 3:
            PIN_HIGH_A = 23
        elif PIN_HIGH_A == 4:
            PIN_HIGH_A = 24
        elif PIN_HIGH_A == 5:
            PIN_HIGH_A = 25
        elif PIN_HIGH_A == 6:
            PIN_HIGH_A = 8
        
    elif PIN_HIGH_P == 6:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH_P = 6   
        
        if PIN_HIGH_A == 0:
            PIN_HIGH_A = 14
        elif PIN_HIGH_A == 1:
            PIN_HIGH_A = 15
        elif PIN_HIGH_A == 2:
            PIN_HIGH_A = 18
        elif PIN_HIGH_A == 3:
            PIN_HIGH_A = 23
        elif PIN_HIGH_A == 4:
            PIN_HIGH_A = 24
        elif PIN_HIGH_A == 5:
            PIN_HIGH_A = 25
        elif PIN_HIGH_A == 6:
            PIN_HIGH_A = 8     
        
    elif PIN_HIGH_P == 7:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH_P = 13
        
        if PIN_HIGH_A == 0:
            PIN_HIGH_A = 14
        elif PIN_HIGH_A == 1:
            PIN_HIGH_A = 15
        elif PIN_HIGH_A == 2:
            PIN_HIGH_A = 18
        elif PIN_HIGH_A == 3:
            PIN_HIGH_A = 23
        elif PIN_HIGH_A == 4:
            PIN_HIGH_A = 24
        elif PIN_HIGH_A == 5:
            PIN_HIGH_A = 25
        elif PIN_HIGH_A == 6:
            PIN_HIGH_A = 8
        
    else:
        for pin in pins_P:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        for pin in pins_P_A:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)            
        print("All Done")
        break  
    

    GPIO.output(PIN_HIGH_P, GPIO.HIGH)
    GPIO.output(PIN_HIGH_A, GPIO.HIGH)
    print("GPIO "+str(PIN_HIGH_P)+" & "+str(PIN_HIGH_A)+" set HIGH")
