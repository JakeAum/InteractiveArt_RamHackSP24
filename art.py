# Jacob Auman
# RamHack SP24 - Interactive Art

# 2 HR Speed Build  2/8/24

# I want to build a script that turns live webcam feed into an ASCII character representation

#####################################################

# Libraries
import cv2
import numpy as np
#import matplotlib.pyplot as plt
import keyboard
from time import sleep

# Constants
WIDTH = 75
HEIGHT = 50


# Functions
def convert_to_ascii(c,brightness):
    # Convert each pixel brightness to an ASCII character
    if c == 1:
        charSET = ".~+:!&$%@#"  # 10 Characters ordered Light -> Dark
    else:
        charSET = "#@%$&!:++~."  # 10 Characters ordered Dark -> Light
    char = charSET[int(brightness/25.5)]  # Brightness Value 0 and 255 spilt into 10 equal intervals
    return char


def main():
    # Open webcam
    cap = cv2.VideoCapture(0)
    c = 0
    while True:
        # Read webcam feed
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        resized = cv2.resize(gray, (WIDTH, HEIGHT))
        
        # Display resized in a live Open CV window
        # For each pixel in resized, calculate the brightness and convert to ASCII
        ascii_image = []

        for col in range(HEIGHT):
        
            ascii_row = []
            
            for row in range(WIDTH):
                
                # Take the Pixel in the col and row and calculate the greyscale brightness value
                brightness = resized[col][row]

                # Convert the brightness to an ASCII character using the convert_to_ascii function
                ascii_char = convert_to_ascii(c,brightness)

                # Append the ASCII character to the row
                ascii_row.append(ascii_char)

            # Assign the row to the corresponding row in the ASCII image
            ascii_image.append(ascii_row)

        # Print the ASCII image to the console
        for row in ascii_image:
            print("".join(row))

        if keyboard.is_pressed('space'):
            if c == 0:
                c = 1
            else:
                c = 0

        if cv2.waitKey(1) & 0xFF == ord('q') or keyboard.is_pressed('q'):
            break

        sleep(0.06)

    # Release webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

