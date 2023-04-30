import pyautogui, pyperclip, time, sys, os
from turtle import *

sys.path.append('../helpers')
from helpers.message import error, success, yellow
from helpers.readImage import readImage

def scanScreen():
    while True:
        import turtle
        # turtle.TurtleScreen._RUNNING = True  # SI NO ANDA, COMENTAR
        # turtle.colormode(255)  # ('red') SI NO ANDA, COMENTAR
        speed(100)
        setup(450, 200, 0, 0)
        colormode(255)
        title("Prosecutor Toolkit")
        pensize(3)
        hideturtle()
        Xscreen, Yscreen = pyautogui.size()
        sc = turtle.Screen()
        turtle = getturtle()
        sc.setup(Xscreen, Yscreen)

        scan_root = (turtle
            ._screen
            .getcanvas()
            .winfo_toplevel())
        scan_root.attributes('-alpha', 0.3)

        Xscreen = Xscreen/2 +10
        Yscreen = Yscreen/2 +30

        seconds = 2
        while seconds > 0:
            write(seconds, False, "center", ("arial", 40, "bold italic"))
            seconds -= 1
            time.sleep(1)
            turtle.clear()

        xbig = 0
        xmin = 9999
        ybig = 0
        ymin = 9999

        penup()
        value = 0
        while value < 1.5:
            x, y = pyautogui.position()
            if x > xbig: xbig = x
            if x < xmin: xmin = x
            if y > ybig: ybig = y
            if y < ymin: ymin = y
            xg = x -(Xscreen/2)          #agregue el /2 porque quedaba desviado sino
            yg = -y +Yscreen
            goto(xg,yg)
            dot(25, 255, 0, 0)
            time.sleep(.1)
            value = value + .1
            pendown()

        time.sleep(.5)
        turtle.clear()
        scan_root.destroy()

        if xmin > xbig and ymin > ybig:
            width = xmin - xbig
            height = ymin - ybig
            screenshot = pyautogui.screenshot(region=(xbig, ybig, width, height))
        elif xmin < xbig and ymin > ybig:
            width = xbig - xmin
            height = ymin - ybig
            screenshot = pyautogui.screenshot(region=(xmin, ybig, width, height))
        elif xmin < xbig and ymin < ybig:
            width = xbig - xmin
            height = ybig - ymin
            screenshot = pyautogui.screenshot(region=(xmin, ymin, width, height))
        elif xmin > xbig and ymin < ybig:
            width = xmin - xbig
            height = ybig - ymin
            screenshot = pyautogui.screenshot(region=(xbig, ymin, width, height))
        else:
            error("No portion of the screen is selected.")
            break

        filename = os.path.join(os.getcwd(), 'temp.png')
        screenshot.save(filename)
        text = readImage(filename)
        os.remove(filename)
        pyperclip.copy(text)
        if text:
            success('Your text is in the clipboard!')
            yellow('\nText: ' + text)
        else:
            error('We cant read the screen.\nNote that if you use Ubuntu 20.04 or above, to use this functionality you must Switch back to Xorg. More info at: https://support.hubstaff.com/screenshot-capture-support-wayland-linux/')
        break