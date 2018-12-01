# imports
import RPi.GPIO as GPIO
import time
import random

# GPIO INITIALIZE
GPIO.setmode(GPIO.BCM)

# GPIO INITIALIZE PINS
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# TURN OFF LEDS
GPIO.output(26, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

# Variables to keep track of state
engine = 'var.engine'
controlRoom = 'var.controlRoom'
gun = 'var.gun'

# 90% success
def chance90():
    number = random.randint(1, 10)
    if number <= 9:
        return 1
    else:
        return 0

# 60% success
def chance60():
    number = random.randint(1, 10)
    if number <= 6:
        return 1
    else:
        return 0

# Check engineHit
def engineHit():
    enginee = open(engine)
    enginee.seek(0)
    engineV = enginee.read()
    return engineV

# Check controlHit
def controlHit():
    cR = open(controlRoom)
    cR.seek(0)
    cRv = cR.read()
    return cRv

# Check gunHit
def gunHit():
    gunns = open(gun)
    gunns.seek(0)
    gunV = gunns.read()
    return gunV

# Check if game has been won
def winCheck():
    if engineHit() == '1' and controlHit() == '1' and gunHit() == '1':
        return 1
    else:
        return 0
# Celeberate once game has been ended

# MAIN LOOP
while True:

    # Variables connected to physical pins
    blaster60 = GPIO.input(23)
    blaster90 = GPIO.input(24)
    targetEngine = GPIO.input(17)
    targetControlRoom = GPIO.input(27)
    fire = GPIO.input(18)

    if fire == False:
        hit = 0
        if blaster60 == False:
            print('Blaster 60 active')
            hit = chance60()
        elif blaster90 == False:
            print('Blaster 90 active')
            hit = chance90()
        if hit == 1:
            if targetControlRoom == False and targetEngine == False and gunHit() == '0':
                print('Hit enemy Gun')
            elif targetControlRoom == False and controlHit() == '0':
                print('Hit enemy Control Room')
            elif targetEngine == False and engineHit() == '0':
                print('Hit enemy Engine')
            else:
                print('No target selected')
            print('hit')
        else:
            print('miss')
        print(winCheck())
        time.sleep(5)


    
