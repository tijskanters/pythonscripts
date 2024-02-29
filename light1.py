# Import the time, wiringpi and sys modules
import time
import wiringpi
import sys

# Define a function called blink that takes a pin number as an argument
def blink(_pin):
   wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin, which turns on the LED
   time.sleep(0.5)                   # Wait for 0.5 seconds
   wiringpi.digitalWrite(_pin, 0)    # Write 0 ( LOW ) to pin, which turns off the LED
   time.sleep(0.5)                   # Wait for another 0.5 seconds

# Initialize the wiringpi library and set pin 2 to output mode
print("Start")                        # Print "Start" to the console
pin = 2                               # Assign the value 2 to the variable pin
wiringpi.wiringPiSetup()              # Initialize the wiringpi library
wiringpi.pinMode(pin, 1)              # Set pin 2 to mode 1 ( OUTPUT ), which means it can send signals

# Blink the LED connected to pin 2 for 10 times
for i in range(0,10):                 # Create a loop that repeats 10 times
   blink(pin)                        # Call the blink function with pin 2 as the argument

# Print "Done" to the console when the loop is finished
print("Done")                         # Print "Done" to the console when the loop is finished