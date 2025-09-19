import pyautogui
import time
import os

# Text to type automatically
text = "Hello, this is an automated typing script!"


def type_in_input_field(text):
	print("You have 10 seconds to focus the input field...")
	time.sleep(10)
	print("Typing repeatedly. Press Ctrl+C to stop.")
	try:
		while True:
			pyautogui.write(text, interval=0.3)
			pyautogui.press('enter')
			time.sleep(2)
	except KeyboardInterrupt:
		print("\nTyping stopped by user.")




def main():
	type_in_input_field(text)

if __name__ == "__main__":
	main()
