import pyautogui
import os

os.chdir(r"C:\Users\Shyrine\Pictures")

# pyautogui.press('win')
print(pyautogui.locateCenterOnScreen('pyautogui_screenshot_vscode.png', minSearchTime=5.0))
pyautogui.click(1159, 1043)
pyautogui.click(525, 31, duration=1.00)
pyautogui.hotkey('ctrl', 'n')
pyautogui.click(344, 123, duration=1.00)
pyautogui.write('Pyt', interval=1.0)
pyautogui.press('enter')
pyautogui.write(r'print("Hello World!")')
pyautogui.hotkey('ctrl', 's', interval=1.0)
pyautogui.press('optionleft', interval=1.0)
pyautogui.press('enter', interval=1.0)
pyautogui.press('f5', interval=1.0)
pyautogui.press('enter')
pyautogui.press('f5', interval=1.0)
