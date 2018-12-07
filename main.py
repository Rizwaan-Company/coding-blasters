# imports
import RPi.GPIO as GPIO
import time
import random
from subprocess import Popen

# SETTING
lightButton = 1
lightPin = 22
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
if lightButton == 1:
    GPIO.setup(lightPin, GPIO.OUT)
    GPIO.output(lightPin, GPIO.HIGH)

# TURN OFF LEDS
def offAll():
    GPIO.output(26, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

# Ensure all LEDS are off
offAll()

# Variables to keep track of state
engine = 'var.engine'
controlRoom = 'var.controlRoom'
gun = 'var.gun'

# Replace to zero
def varZero():
    wr = open(engine, 'w')
    wr.write('0')
    wr.close()
    wr = open(controlRoom, 'w')
    wr.write('0')
    wr.close()
    wr = open(gun, 'w')
    wr.write('0')
    wr.close()

# Dance
def dance():
    offAll()
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.5)

# Celebrate
def celeberate():
    offAll()
    time.sleep(1)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(19, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    dance()
    dance()
    dance()
    dance()
    offAll()
    varZero()

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
        return True
    else:
        return False
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
        weaponSEL = 0
        if blaster60 == False:
            print('Blaster 60 active')
            hit = chance60()
            weaponSEL = 1
        elif blaster90 == False:
            print('Blaster 90 active')
            hit = chance90()
            weaponSEL = 2
        if hit == 1:
            print('gun ')
            print(gunHit())
            print('cr ')
            print(controlHit())
            print('eng ')
            print(engineHit())
            if targetControlRoom == False and targetEngine == False and gunHit() == '0':
                print('Hit enemy Gun')
                if weaponSEL == 1:
                    Popen(['python', 'gun60.py'])
                if weaponSEL == 2:
                    Popen(['python', 'gun90.py'])
            elif targetControlRoom == False and controlHit() == '0':
                print('Hit enemy Control Room')
                if weaponSEL == 1:
                    Popen(['python', 'cr60.py'])
                if weaponSEL == 2:
                    Popen(['python', 'cr90.py'])
            elif targetEngine == False and engineHit() == '0':
                print('Hit enemy Engine')
                if weaponSEL == 1:
                    Popen(['python', 'eng60.py'])
                if weaponSEL == 2:
                    Popen(['python', 'eng90.py'])
            else:
                print('No target selected')
            print('hit')
        else:
            print('miss')

        if lightButton == 1:
            GPIO.output(lightPin, GPIO.LOW)
            print("win check")
            print(winCheck)
            if winCheck() == True:
                celeberate()
            time.sleep(5)
            GPIO.output(lightPin, GPIO.HIGH)
        else:    
            time.sleep(5)


    
