#! python3
# Display the mouse cursor's current position

import pyautogui

def main (rgb = False, hsv = False): 

    print ('Press CTRL+C to quit.')

    try: 
        while True: 
            # Get and print the mouse coordinates
            x, y = pyautogui.position()
            positionStr = 'X: %s Y: %s' % (str(x).rjust(4), str(y).rjust(4))
            pixelColorRGB = pyautogui.screenshot().getpixel((x,y))
            pixel_r = pixelColorRGB[0]
            pixel_g = pixelColorRGB[1]
            pixel_b = pixelColorRGB[2]
            pixelColorHSV = rgb_to_hsv (pixel_r, pixel_g, pixel_b)


            if rgb: 
                positionStr += '\t RGB: (%s, %s, %s)' % (str(pixelColorRGB[0]).rjust(3), \
                    str(pixelColorRGB[1]).rjust(3), str(pixelColorRGB[2]).rjust(3))

            if hsv: 
                positionStr += '\t HSV: (%s, %s, %s)' % (str(pixelColorHSV[0])[0:5].rjust(5), \
                    str(pixelColorHSV[1])[0:5].rjust(5), str(pixelColorHSV[2])[0:5].rjust(5))
            
            print (positionStr, end='')
            print ('\b' * len(positionStr), end='', flush=True) # Delate the las print

    except KeyboardInterrupt: 
        print ('\nDone')

def rgb_to_hsv(r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df/mx)*100
        v = mx*100
        return h, s, v

main (rgb = False, hsv = True)