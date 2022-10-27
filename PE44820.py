import RPi.GPIO as GPIO
import time

#Contorolled pin number
PIN_HIGH =0
P_or_S = 20
OPT = 21
#Set GPIO mode
#라즈베리파이 핀 번호를 GPIO 번호로 사용
#GPIO.setmode(GPIO.BOARD)
#회로의 GPIO 번호 사용
GPIO.setmode(GPIO.BCM)

#Set GPIO Pin
#GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(P_or_S, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(OPT, GPIO.OUT, initial=GPIO.LOW)
list = [23,25] #of list =(3,5)
GPIO.setup(list, GPIO.OUT, initial=GPIO.LOW)

#Controll Pin
GPIO.output(P_or_S, GPIO.LOW)
GPIO.output(OPT, GPIO.LOW)
GPIO.output(PIN_HIGH, GPIO.HIGH)
time.sleep(1)



GPIO.setup(gpio_num, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_num, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



#reset
GPIO.cleanup()