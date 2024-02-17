# Jacob Auman
# RamHack SP24 - Interactive Art

# 2 HR Speed Build  2/8/24

# I want to build a script that turns live webcam feed into an ASCII character representation

#####################################################

import cv2
import numpy as np
import keyboard
from time import sleep

WIDTH = 120
HEIGHT = 90

def convert_to_ascii(c, brightness):
    charSET = ".~+:!&$%@#"  # 10 Characters ordered Light -> Dark
    index = int(brightness / 25.5)
    if index >= len(charSET):
        index = len(charSET) - 1
    char = charSET[index]
    return char

def contrast_stretching(image):
    # Convert image to grayscale
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply contrast stretching
    min_val = np.min(image)
    max_val = np.max(image)
    stretched = cv2.convertScaleAbs(image, alpha=255.0/(max_val-min_val), beta=-255.0*min_val/(max_val-min_val))

    return stretched


def main():
    cap = cv2.VideoCapture(0)
    c = 1  # 1 for Light -> Dark, 0 for Dark -> Light

    while True:
        blk_image = np.zeros((800, 1200, 3), np.uint8)
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        stretched = contrast_stretching(gray)  # Apply contrast stretching
        # cv2.imshow('frame', frame)
        resized = cv2.resize(stretched, (WIDTH, HEIGHT))
        ascii_image = []

        for col in range(HEIGHT):
            ascii_row = []
            for row in range(WIDTH):
                brightness = resized[col][row]
                ascii_char = convert_to_ascii(c, brightness)
                ascii_row.append(ascii_char)
            ascii_image.append(ascii_row)

        for y, row in enumerate(ascii_image):
            for x, char in enumerate(row):
                cv2.putText(blk_image, char, (x * 10, y * 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.imshow('ASCII', blk_image)

        # if keyboard.is_pressed('space'):
            

        if cv2.waitKey(1) & 0xFF == ord('q') or keyboard.is_pressed('q'):
            break

        sleep(0.01)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

