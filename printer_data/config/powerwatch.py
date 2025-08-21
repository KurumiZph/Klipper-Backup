import RPi.GPIO as GPIO
import time

PIN = 17   # GPIO pin you connected

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(PIN) == 0:  # LOW = power loss
            print("Power loss detected! (would shutdown here)")
            # os.system("sudo shutdown -h now")  <-- disabled for testing
            break
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
