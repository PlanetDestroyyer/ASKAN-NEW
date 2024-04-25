import serial
import time
from decimal import Decimal

try :
# Initialize serial communication
    ser = serial.Serial('COM7', 9600)  # Replace 'COM4' with your Arduino's serial port

    # Thresholds
    lowerThreshold = 310
    upperThreshold = 510

    # Function to print water level message
    def print_water_level_message(level):
        if level <= 0:
            print("Water Level: need more water")
        elif 0 < level <= 400:
            print("Water Level: need water")
        else:
            print("Water Level: full")

    # Loop
    while True:
        # Read water level from the Arduino

        line = ser.readline().decode().rstrip()

        new_line = int(float(line[-1]))

        if line:
            waterLevel = int(new_line)  
            print_water_level_message(waterLevel)

                # print(line)  # Print any non-integer lines received from the Arduino
        else:
            print("The sensors are not connected or reload the website")

        time.sleep(1)
except :
    print("Connect the sensor")
    
if __name__ == "main":
    pass