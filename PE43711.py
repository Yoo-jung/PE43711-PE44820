import RPi.GPIO as GPIO
import time

# Declare the pin number
PIN_HIGH = 0
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
pins = [D0, D1, D2, D3, D4, D5, D6, D7]

# Set GPIO mode
#라즈베리파이 핀 번호를 GPIO 번호로 사용
#GPIO.setmode(GPIO.BOARD)
#회로의 GPIO 번호 사용
GPIO.setmode(GPIO.BCM)

# Set GPIO Pin
GPIO.setup(P_or_S, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(OPT, GPIO.OUT, initial=GPIO.LOW)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
time.sleep(2)
print("Initial setup complete")

# Controll Pin
GPIO.output(P_or_S, GPIO.LOW)
GPIO.output(OPT, GPIO.LOW)
while (True):
    PIN_HIGH = int(input("PIN Number to set HIGH: "))
    if PIN_HIGH == 0:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH = 22
    elif PIN_HIGH == 1:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH = 10
    elif PIN_HIGH == 2:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH = 9
    elif PIN_HIGH == 3:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH = 11
    elif PIN_HIGH == 4:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH = 0        
    elif PIN_HIGH == 5:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH = 5
    elif PIN_HIGH == 6:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH = 6        
    elif PIN_HIGH == 7:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        PIN_HIGH = 13
    else:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
            print("GPIO"+str(pin)+"Down.")
        print("All Done")
        break        
    GPIO.output(PIN_HIGH, GPIO.HIGH)
    print("GPIO "+str(PIN_HIGH)+" set HIGH")
    



#GPIO.setup(gpio_num, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(gpio_num, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# reset
#GPIO.cleanup()
