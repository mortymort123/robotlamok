import RPi.GPIO as GPIO # import RPi.GPIO module  
from time import sleep             # lets us have a delay  

leftForward = 29
rightForward = 31
leftBackward = 33
rightBackward = 35

def setup():
    global PWM_LEFTFRONT,PWM_RIGHTFRONT,PWM_LEFTBACK,PWM_RIGHTBACK
    GPIO.setmode(GPIO.BOARD)                      # choose BCM or BOARD  
    GPIO.setup(leftForward, GPIO.OUT)           # left foward    
    GPIO.setup(leftBackward, GPIO.OUT)          # left backward
    GPIO.setup(rightForward, GPIO.OUT)          # right forward 
    GPIO.setup(rightBackward, GPIO.OUT)         # right backward


    PWM_LEFTFRONT = GPIO.PWM(12,400)                 # leftfront speed
    PWM_RIGHTFRONT = GPIO.PWM(11,400)                # rightfront speed
    PWM_LEFTBACK = GPIO.PWM(13,400)                 # leftback speed
    PWM_RIGHTBACK = GPIO.PWM(15,400)                # rightback speed
    
    PWM_LEFTFRONT.start(0)
    PWM_RIGHTFRONT.start(0)
    PWM_LEFTBACK.start(0)
    PWM_RIGHTBACK.start(0)

    PWM_LEFTFRONT.ChangeDutyCycle(70)
    PWM_RIGHTFRONT.ChangeDutyCycle(70)
    PWM_LEFTBACK.ChangeDutyCycle(70)
    PWM_RIGHTBACK.ChangeDutyCycle(70)


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
        GPIO.cleanup()

def moveForward(move):
    GPIO.output(leftForward,move)
    GPIO.output(rightForward,move)

def moveBackward(move):
    GPIO.output(leftBackward,move)
    GPIO.output(rightBackward,move)

def rotateLeft(move):
    GPIO.output(leftBackward,move)
    GPIO.output(rightForward,move)
    
def rotateRight(angle):
    GPIO.output(leftForward,angle)
    GPIO.output(rightBackward,angle)

setup()
loop()
