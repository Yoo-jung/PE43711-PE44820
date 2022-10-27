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
    PIN_HIGH = input("PIN Number to set HIGH: ")
    GPIO.output(PIN_HIGH, GPIO.HIGH)
    
    if PIN_HIGH == "out":
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
            print("Done.")
        break




#GPIO.setup(gpio_num, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(gpio_num, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# reset
#GPIO.cleanup()
