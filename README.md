# Vigilant Fiesta

A minimalist automation toolkit for mouse and keyboard actions using Python.

## Features
- Automated mouse cursor movement (`auto_move_cursor.py`)
- Automated keyboard typing (`auto_typing.py`)

## Usage
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pyautogui
   ```
2. Run the desired script:
   - Move cursor: `python auto_move_cursor.py`
   - Automated typing: `python auto_typing.py`

## Requirements
- Python 3.x
- pyautogui

## Notes
- For typing automation, focus the input field within the given time.
- Press `Ctrl+C` to stop any script.
