import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

ss = crickit.seesaw

num_pixels = 24  # Number of pixels driven from Crickit NeoPixel terminal

# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)        
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLANK = (0, 0, 0)

#tell pi to listen for potentiometer signals here:
pot = crickit.SIGNAL2
# establish the pin mode of our variable "pot" as input
ss.pin_mode(pot, ss.INPUT)

def check_pot():
    #this is a very simple function - we
    #read the value of the potentiometer ...
    potValue = ss.analog_read(pot)
    #... print the value ...
    print("Pot value ", potValue)
    #... and send that value back to where the function was called!
    return potValue

def conditional():
    #1.1. we'll start with conditionals!
    #in python, indentation & tabs are crucial! 
    
    #this first line calls the 'check_pot' function.
    #if the value returned is greater than 520 - halfway
    #turned - then we turn the light purple. 
    if(check_pot() > 520):
        blink(1)
    #this next line is an 'else' statement - what happens if
    #the previous condition is not met. In this case, we
    #turn the LED blank. 
    else:
        pixels.fill(BLANK)
        
def blink(dur):
    #turn the LED on and off twice
    #separated by the duration indicated by the dur
    #variable
    pixels.fill(PURPLE)
    time.sleep(dur)
    pixels.fill(BLANK)
    time.sleep(dur)
    pixels.fill(PURPLE)
    time.sleep(dur)
    pixels.fill(BLANK)
    time.sleep(dur)

def while_function():
    #1.2
    #a while loop runs instructions until conditions are no longer met.
    
    #the first line of a while statement sets up the conditions to run
    #in this case, as long as the potentiometer reads above 50, run
    #blink the LED 
    while check_pot() > 520:
        blink(1)
    #similar to the conditional, once the condition is no longer met, run the
    #else instructions
    else:
        pixels.fill(BLANK)

def for_function():
    #1.3
    #a for loop runs instructions over each element of a sequence.
    
    #an array containing some fun colors we defined earlier. note that these
    #are variables
    colors = [RED, YELLOW, GREEN, PURPLE, BLUE]
    
    #the first line of a for statement sets up the sequence to run over
    #in this case, we'll sequence through five colors, waiting a second
    #in between each. note that color in colors means that the color variable
    #takes the value of each index of the array colors. 
    for color in colors:
        pixels.fill(color)
        time.sleep(1)
    
    #In this second example, we create a 'range' - that is a vector from
    #1 to 5, in this case specified by the number in range
    #The instructions will execute 3 times
    for x in range(3):
       blink(1)

    
    pixels.fill(BLANK)

#main is the default function that will run! 
def main():

    #conditional()
        
    #while_function()
    for_function()
    
    #wait five seconds ...
    time.sleep(5)
    #... now shut off the light!
    pixels.fill(BLANK)

    
if __name__ == '__main__':
        main()    

