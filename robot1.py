import lgpio # import RPi.GPIO module  
from time import sleep             # lets us have a delay  

leftForward = 1
rightForward = 0
leftBackward = 2
rightBackward = 3   

h = lgpio.gpiochip_open(0)


def setup():
    lgpio.tx_pwm(h, 21, 400, 70)
    lgpio.tx_pwm(h, 22, 400, 70)
    lgpio.tx_pwm(h, 23, 400, 70)
    lgpio.tx_pwm(h, 24, 400, 70)
    

def loop():
    try:  
        while True:  
            moveForward(1)
            sleep(1)
            moveForward(0)
            sleep(1)
            moveBackward(1)
            sleep(1)
            moveBackward(0)
            sleep(1)
            rotateLeft(1)
            sleep(1)
            rotateLeft(0)
            sleep(1)
            rotateRight(1)
            sleep(1)
            rotateRight(0)
            sleep(1)
                     # wait half a second  
    except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
        lgpio.gpiochip_close(h)

def moveForward(move):
    lgpio.gpio_write(h,leftForward,move)
    lgpio.gpio_write(h,rightForward,move)

def moveBackward(move):
    lgpio.gpio_write(h,leftBackward,move)
    lgpio.gpio_write(h,rightBackward,move)
    

def rotateLeft(move):
    lgpio.gpio_write(h,leftBackward,move)
    lgpio.gpio_write(h,rightForward,move)
    
    
def rotateRight(move):
    lgpio.gpio_write(h,leftForward,move)
    lgpio.gpio_write(h,rightBackward,move)

setup()
loop()
