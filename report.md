# Automation Scripts Report

## Project: Vigilant Fiesta

### Overview
This project provides two minimalist Python scripts for automating mouse and keyboard actions:
- `auto_move_cursor.py`: Moves the mouse cursor randomly across the screen at set intervals.
- `auto_typing.py`: Types a predefined message into any focused input field repeatedly until interrupted.

### Implementation Details
- **Language:** Python 3
- **Dependencies:** `pyautogui` (install via pip)
- **Virtual Environment:** Recommended for dependency isolation

#### `auto_move_cursor.py`
- Moves the mouse cursor to random screen positions every 3 seconds.
- Runs in an infinite loop until interrupted by the user (Ctrl+C).
- Uses a `main()` function for script entry.

#### `auto_typing.py`
- Types a preset message into the currently focused input field.
- Waits 10 seconds before starting to allow the user to focus the input field.
- Types the message repeatedly with a delay between repetitions.
- Runs until interrupted by the user (Ctrl+C).
- Uses a `main()` function for script entry.

### Usage Instructions
1. Set up a Python virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pyautogui
   ```
2. Run the desired script:
   - Move cursor: `python auto_move_cursor.py`
   - Automated typing: `python auto_typing.py`

### Observations
- Both scripts are minimalist and easy to use.
- The user can stop the automation at any time with Ctrl+C.
- The scripts are cross-platform but tested on macOS.

### Recommendations
- Always activate the virtual environment before running the scripts.
- Adjust timing and message as needed for your use case.
- Ensure the input field is focused before automated typing begins.

---
Report generated on 19 September 2025.
