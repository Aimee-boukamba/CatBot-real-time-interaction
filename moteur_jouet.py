import RPi.GPIO as GPIO

# Configuration des broches GPIO
M1A = 17
M1B = 27

# Initialisation des broches
GPIO.setmode(GPIO.BCM)
GPIO.setup(M1A, GPIO.OUT)
GPIO.setup(M1B, GPIO.OUT)

# Initialisation PWM
pwm = GPIO.PWM(M1A, 1000) 
pwm.start(100)

def forward():
    GPIO.output(M1B, GPIO.LOW)

try:
    forward()  # Fait tourner le moteur en avant en continu
    while True:
        pass  # Boucle infinie pour maintenir le moteur en marche

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
