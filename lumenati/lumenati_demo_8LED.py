#This is demonstration code for the Lumenati line of APA102c boards,
#specifically using (4) 90L boards surrounding one 8-pack board.

import time

from SFE_Lumenati import set_LED_quantity, WriteLEDs, set_LED

#Set up array, 8 LEDs
set_LED_quantity(8)

#Delay duration
wait = 0.15

#Global brightness
brightness = 15 #range is 0-31



# Cycle white through the LEDs

try:
    while True:

        for y in range (8):
            
            # white
            set_LED(x,25,25,25,brightness)

            #Write to the LEDs and wait
            WriteLEDs()
            time.sleep(wait)


except KeyboardInterrupt:
    pass


