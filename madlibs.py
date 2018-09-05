from time import sleep
import sys

# Inspiried by Asim and Ikey
# delaying print - effect
def delay_print(string):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)  
    print('')
    return ">>"
    

# assigning green color to my text
green = '\033[32m'
# assigning red color to display user input
red = '\033[31m'

# Intro
delay_print(green + "SEARCHING...")
sleep(2)
delay_print(green + "I see you are awake!")
sleep(1)
delay_print(green + "The Matrix has you now...")
sleep(1)
welcome_text = 'Welcome to the Matrix stranger! I know you have questions and I have answers for them. Ill dive into your subconcious\n for the answers you need. But before I have have to know you better'
delay_print(green + welcome_text.upper())
sleep(1)

# Questions
name = input(delay_print(green + "How do they call you in non-digital realm? "))
sleep(1)
delay_print(green + "Not bad! If you reach Zion, you will be assigned your digital name.")
sleep(1)
restaurant = input(delay_print("Which restaurant is your favorite? "))
sleep(1)
color = input(delay_print("Type the first color came to your mind "))
sleep(1)
animal = input(delay_print("Which animal scares you the most? "))
sleep(1)
car = input(delay_print("Your dream car "))
sleep(1)
street = input(delay_print("Type the street name that you live "))
sleep(1)

# Final text
print(red + "Request sent")
sleep(1)
delay_print(red + "Receiving response from Zion...")
sleep(1)
print(red + "Here is the message from Morphius:")

delay_print(green + "I salute you " + red + name + "! " + green +
            "You cheated the system and enrolled to Make School to join other hackers. Merovingian announced\n a reward for your codes. " 
            "The agents are waiting for your at " + red + restaurant + green +". Don’t go there anymore. Stay awake and look for " 
            + red + color+ " " + animal + green +".\n It will lead you to Trinity. She will be in " + red + color+ " " +car + green + " at " + red + street + green +".\n End of line...")

exit()


# REQUIREMENTS

# User Requrements:
# 1. User should be able to make several inputs
# 2. User should be able to see diplayed full text, where his/her inputs
#     are colored

# Functional Requirements
# 1. The app should be able to recieve and store user inputs
# 2. The app should be able to fill in the text with specific user inputs


# Matrix white rabbit scene
# starts with SEARCHING...
# Wake up Neo
# The Matrix has you...
# ENDS with
# Follow the white rabbit
#  Knock, knock, Neo.
