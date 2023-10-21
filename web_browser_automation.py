import pyautogui
import time

# Delay to give you time to focus on the target window
time.sleep(5)

# Example: Automate opening a web browser and a website
pyautogui.press('win')  # Press the Windows key
pyautogui.write('chrome')  # Type the name of the browser (e.g., Chrome)
pyautogui.press('enter')  # Press Enter
time.sleep(2)  # Wait for the browser to open

# You can automate other tasks, like opening a website
pyautogui.write('https://www.example.com')
pyautogui.press('enter')
time.sleep(5)

# For more advanced automation, you can control the mouse and keyboard
# Example: Automate moving the mouse and clicking
pyautogui.moveTo(500, 500)  # Move the mouse to (500, 500) on the screen
pyautogui.click()  # Click the mouse

# You can also automate keyboard input
pyautogui.write('Hello, world!')

# Close the browser (this may vary depending on the browser)
pyautogui.hotkey('ctrl', 'w')  # Close the current tab
pyautogui.hotkey('ctrl', 'shift', 'w')  # Close the browser (all tabs)

# Note: Be cautious when automating tasks as it can have unintended consequences.
