import pyautogui
pyautogui.click(10, 5,button='left')
"""
**You can also perform a click by calling pyautogui.mouseDown(), which
  only pushes the mouse button down, and pyautogui.mouseUp(), which
  only releases the button. These functions have the same arguments as
  click(), and in fact, the click() function is just a convenient
  wrapper around these two function calls.

**As a further convenience, the pyautogui.doubleClick() function will
  perform two clicks with the left mouse button, while the
  pyautogui.rightClick() and pyautogui.middleClick() functions will
  perform a click with the right and middle mouse buttons, respectively.

"""