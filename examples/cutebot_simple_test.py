# cutebot_simple_test.py
#Version: 2.0
# Author: James Tobin

######################################################
#   Import
######################################################
import time
from jisforjt_cutebot_clue import cutebot, clue


######################################################
#   Variables
######################################################
clue.sea_level_pressure = 1020                              # Set sea level pressure for Clue's Altitude sensor.


######################################################
#   Functions
######################################################

def cutebot_Sensors():
    print("Sonar: {:.2f}".format(cutebot.sonar))
    s_left, s_right = cutebot.tracking
    print("Left Line Tracking: {}".format(s_left))
    print("Right Line Tracking: {}".format(s_right))
    print("P1: {}".format(cutebot.p1))
    print("P2: {}".format(cutebot.p2))
    print("----------------------------------")

def clue_Sensors():
    print("Acceleration: {:.2f} {:.2f} {:.2f} m/s^2".format(*clue.acceleration))
    print("Gyro: {:.2f} {:.2f} {:.2f} dps".format(*clue.gyro))
    print("Magnetic: {:.3f} {:.3f} {:.3f} uTesla".format(*clue.magnetic))
    print("Pressure: {:.3f} hPa".format(clue.pressure))
    print("Altitude: {:.1f} m".format(clue.altitude))
    print("Temperature: {:.1f} C".format(clue.temperature))
    print("Humidity: {:.1f} %".format(clue.humidity))
    print("Proximity: {}".format(clue.proximity))
    print("Gesture: {}".format(clue.gesture))
    print("Color: R: {} G: {} B: {} C: {}".format(*clue.color))
    print("----------------------------------")


######################################################
#   Main Code
######################################################

while True:
    """
    Uncomment the sensor function you want to test below.
    """

    cutebot_Sensors()
    #clue_Sensors()
    
    time.sleep(2) # Wait for two seconds
    
    if clue.button_a:
        break
print("========== End ==========")
