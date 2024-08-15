import pyautogui

pyautogui.click(232,410, interval=0.5)
pyautogui.press('space')

while True:
   print(pyautogui.pixel(232,410))
   if pyautogui.pixelMatchesColor(232,410,[83,83,83],70):
        pyautogui.press('space')

   elif pyautogui.pixelMatchesColor(230,395,[83,83,83],70):
        print(pyautogui.pixel(232,395))
        pyautogui.press('down',interval=2)        