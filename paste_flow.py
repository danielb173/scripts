import time
import pyperclip
import pyautogui

# Introduce short delay for the script to ensure the scripts shortcut has been pressed and released fully
time.sleep(1)

# Get the clipboard content using pyperclip
original_clipboard = pyperclip.paste()

# Check if the clipboard contains commas, spaces, or newlines
if ',' in original_clipboard and ' ' in original_clipboard:
    # Prioritize commas and remove spaces
    original_clipboard = original_clipboard.replace(' ', '')
    items = original_clipboard.split(',')
elif ',' in original_clipboard:
    # If only commas are found, split by commas
    items = original_clipboard.split(',')
elif ' ' in original_clipboard:
    # If only spaces are found, split by spaces
    items = original_clipboard.split(' ')
elif '\n' in original_clipboard or '\r\n' in original_clipboard:
    # If newlines are found, split by newlines
    items = original_clipboard.split('\n') if '\n' in original_clipboard else original_clipboard.split('\r\n')
else:
    # If none of the above, assume a single item
    items = [original_clipboard]

# Iterate through each item
for item in items:
    # Check if the item is non-empty
    if item.strip():
        # Copy the current item to the clipboard
        pyperclip.copy(item)

        # Introduce a short delay before pasting
        time.sleep(0.1)

        # Paste the current item
        pyautogui.hotkey("ctrl", "v")

        # Introduce a short delay after pasting
        time.sleep(0.1)

        # Press Enter
        pyautogui.press("enter")

        # Introduce a delay after pressing Enter
        time.sleep(0.1)

# Clear the clipboard
pyperclip.copy('')
