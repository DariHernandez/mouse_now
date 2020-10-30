#! python3
# Display the mouse cursor's current position

import pyautogui
print ('Press CTRL+C to quit.')

try: 
    while True: 
        # Get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: %s Y: %s' % (str(x).rjust(4), str(y).rjust(4))
        pixelColor = pyautogui.screenshot().getpixel((x,y))
        positionStr += ' RGB: (%s, %s, %s)' % (str(pixelColor[0]).rjust(3), \
            str(pixelColor[1]).rjust(3), str(pixelColor[2]).rjust(3))
        print (positionStr, end='')
        print ('\b' * len(positionStr), end='', flush=True) # Delate the las print

except KeyboardInterrupt: 
    print ('\nDone')
