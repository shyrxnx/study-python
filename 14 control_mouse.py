import pyautogui

# Set up a pause after you run the program or call PyAutoGUI
pyautogui.PAUSE = 5.0

# Get the position of the mouse
print(pyautogui.position())

# Get the screen resolution
print(pyautogui.size())

# pyautogui.moveTo(0, 0, duration=0.01)

# pyautogui.moveTo(468, 1047, duration=0.20)
pyautogui.click(468, 1047, duration=0.10)
pyautogui.click(592, 460, duration=0.05)
pyautogui.click(901, 462, duration=0.05)
pyautogui.click(307, 346, duration=0.05)
