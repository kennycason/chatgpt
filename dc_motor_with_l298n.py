# Write python code to control dc motor with L298N Motor Driver Controller with reverse and forward

# Import the necessary libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the pin numbers for the L298N Motor Driver Controller
ENA = 25 # 18
IN1 = 24 # 19
IN2 = 23 # 26

# Set the pin numbers for the motor
IN3 = 20 # 13
IN4 = 26 # 6
ENB = 16 # 12

# Set the pins for the L298N Motor Driver Controller as output
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Set the pins for the motor as output
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# Create PWM instances for the L298N Motor Driver Controller
pwmA = GPIO.PWM(ENA, 100)
pwmB = GPIO.PWM(ENB, 100)

# Start the PWM instances
pwmA.start(0)
pwmB.start(0)

# Function to move the motor in the forward direction
def forward():
    # Set the pins for the L298N Motor Driver Controller
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    # Set the pins for the motor
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    # Set the speed of the motor
    pwmA.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(100)

# Function to move the motor in the reverse direction
def reverse():
    # Set the pins for the L298N Motor Driver Controller
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    # Set the pins for the motor
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    # Set the speed of the motor
    pwmA.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(100)

# Continuously move the motor in the forward direction for 5 seconds
while True:
    forward()
    time.sleep(5)
    # Stop the motor
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    # Move the motor in the reverse direction for 5 seconds
    reverse()
    time.sleep(5)
    # Stop the motor
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)

# This code continuously moves the motor in the forward direction for 5 seconds, then stops the motor, moves the motor
# in the reverse direction for 5 seconds, and then stops the motor again. You can adjust the speed of the motor and the
# length of time it is moving in each direction by modifying the ChangeDutyCycle() and `time.sleep