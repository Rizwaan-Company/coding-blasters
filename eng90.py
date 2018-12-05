import time
import RPi.GPIO as GPIO
engine = 'var.engine'
controlRoom = 'var.controlRoom'
gun = 'var.gun'

valueG = 90
pin = 26

stufff = "null"
if pin == 13:
    stufff = gun
elif pin == 19:
    stufff = controlRoom
elif pin == 26:
    stufff = engine

GPIO.setup(pin, GPIO.OUT)
wr = open(stufff, 'w')
wr.write('1')
wr.close()

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


timeIntervals = 0
i = 0
if valueG == 60:
    timeIntervals = 180
elif valueG == 90:
    timeIntervals = 320

breakster = 0
GPIO.output(pin, GPIO.HIGH)

print(gunHit())
while i < timeIntervals:
    time.sleep(0.5)
    if winCheck() == 1:
        breakster = 1
        break
    print(i)
    print(winCheck())
    i += 1

if breakster == 0:
    #GPIO.output(pin, GPIO.LOW)
    wr = open(stufff, 'w')
    wr.write('0')
    wr.close()
