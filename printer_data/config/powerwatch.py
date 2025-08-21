import RPi.GPIO as GPIO
import time

PIN = 17   # GPIO pin you connected

GPIO.setmode(GPIO.BCM)
# Use pull-up so pin won't float if signal not connected
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(PIN) == 0:  # LOW = power loss
            print("⚠️ Power loss detected! (would shutdown here)")
        else:
            print("✅ Power OK")
        time.sleep(5)  # check every 5 seconds
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
