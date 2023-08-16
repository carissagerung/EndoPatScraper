import pyautogui
import pywintypes
import win32api
import win32con

# Path: endoPATscraper.py

# Check screen size

size=pyautogui.size()
print(size) # Size(width=1920, height=1080)

# Change screen size to (1920, 1080) if not already

if size != (1920, 1080):
    pyautogui.alert(text='Please change the screen resolution to 1920 x 1080 before continuing', title='Screen Resolution', button='OK')
    exit()
    
    # This code doesn't work - tried to auto-change screen resolution to 1920 x 1080
    #devmode = pywintypes.DEVMODEType()
    #devmode.PelsWidth = 1900
    #devmode.PelsHeight = 1080
    #devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
    #win32api.ChangeDisplaySettings(devmode, 0) 
    
# Move arrow to change time frame to 15 second blocks



pyautogui.click(x=807,y=66)
pyautogui.click(x=778,y=98)
pyautogui.click(x=891,y=58)
pyautogui.click(x=972,y=54)



# Collect first image of Probe 1
im = pyautogui.screenshot('probe1_1.png',region=(192, 125, 534, 380))  # x,y,width,height

# Collect first image of Probe 2
im = pyautogui.screenshot('probe2_1.png', region=(192, 581, 534, 380 )) # x,y,width,height

# Move to next 5 second interval
pyautogui.click(x=1717,y=1009, clicks=135, interval=0.005)

#Now collect the remaining images
for i in range(2, 180):
    im = pyautogui.screenshot('probe1_'+ str(i) + '.png',region=(192, 125, 534, 380))  # x,y,width,height
    im = pyautogui.screenshot('probe2_' + str(i) +'.png', region=(192, 581, 534, 380 )) # x,y,width,height
    pyautogui.click(x=1717,y=1009, clicks=160, interval=0.005)


