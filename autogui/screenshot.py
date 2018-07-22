import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((50,200)))
print(pyautogui.pixelMatchesColor(50, 200, (51, 51, 51)))