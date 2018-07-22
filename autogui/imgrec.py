import pyautogui
print(pyautogui.locateOnScreen('catlogo.png'))
#will give coordinates of image

#if image found
pyautogui.center((643, 745, 70, 29))
pyautogui.click((678, 759))#coordinates of centre