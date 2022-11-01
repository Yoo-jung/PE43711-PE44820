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
pins_A = [A0, A1, A2, A3, A4, A5, A6]

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
for pin in pins_A:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
time.sleep(2)
print("Initial setup complete")

# Controll Pin
GPIO.output(P_or_S, GPIO.LOW)
GPIO.output(OPT, GPIO.LOW)

print("Start to control GPIO")

for PIN_HIGH_P in range(0, 6, 1):
    time.sleep(5)
    print(PIN_HIGH_P)
    
    if PIN_HIGH_P == 0:
        PIN_HIGH_P = 22
    elif PIN_HIGH_P == 1:
        PIN_HIGH_P = 10
    elif PIN_HIGH_P == 2:
        PIN_HIGH_P = 9
    elif PIN_HIGH_P == 3:
        PIN_HIGH_P = 11
    elif PIN_HIGH_P == 4:
        PIN_HIGH_P = 0     
    elif PIN_HIGH_P == 5:
        PIN_HIGH_P = 5
    elif PIN_HIGH_P == 6:
        PIN_HIGH_P = 6
    elif PIN_HIGH_P == 7:
        PIN_HIGH_P = 13
        
    for PIN_HIGH_A in range(0, 6, 1):
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
    
    for pin in pins_P:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    for pin in pins_A:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        
    GPIO.output(PIN_HIGH_P, GPIO.HIGH)
    GPIO.output(PIN_HIGH_A, GPIO.HIGH)
    print("GPIO "+str(PIN_HIGH_P)+" & "+str(PIN_HIGH_A)+" set HIGH")
