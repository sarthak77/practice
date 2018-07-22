import pyautogui
pyautogui.click()

#writes using keyboard
pyautogui.typewrite("hello world",0.2)

pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
#presses these keys

pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')