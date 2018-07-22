import pyautogui

#to copy
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

"""
This is rather complicated. Instead, use the pyautogui.hotkey()
function, which takes multiple keyboard key string arguments,
presses them in order, and releases them in the reverse order.
"""

pyautogui.hotkey('ctrl', 'c')