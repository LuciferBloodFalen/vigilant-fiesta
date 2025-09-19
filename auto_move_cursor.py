import pyautogui
import time
import random

# Move the mouse cursor in a random pattern every second
try:
    print("Press Ctrl+C to stop the script.")
    while True:
        # Get the screen size
        screen_width, screen_height = pyautogui.size()
        # Generate random coordinates within the screen
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        # Move the mouse to the random position
        pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(3)
except KeyboardInterrupt:
    print("\nScript stopped by user.")
