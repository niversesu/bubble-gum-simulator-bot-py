import subprocess
import sys
import time
import pyautogui
import pyperclip

roblox = pyautogui.press
wait = time.sleep

# --configuration--
w = "w"
s = "s"
a = "a"
d = "d"
m = "m"
e = "e"
b = "b"
space = "space"
shift = "shift"
left = "left"
right = "right"
esc = "esc"
prt = "print screen"
chat = "/"
emote = "."
enter = "enter"

def focus_sober_window():
    """
    Finds and focuses on the window with the title "Sober".
    Returns True if the window was found and focused, False otherwise.
    """
    window_title = "Sober"
    try:
        # List all windows and grep for the window title
        command = ["wmctrl", "-l"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        output, _ = process.communicate()

        window_id = None
        for line in output.splitlines():
            if window_title in line:
                # Extract the window ID, which is the first part of the line
                window_id = line.split()[0]
                break

        if window_id:
            # Activate the window using its ID
            activate_command = ["wmctrl", "-ia", window_id]
            subprocess.run(activate_command, check=True)
            print(f"Focused on window: {window_title}")
            return True
        else:
            print(f"Window with title '{window_title}' not found.")
            return False

    except FileNotFoundError:
        print("Error: wmctrl command not found. Please install wmctrl.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error executing wmctrl command: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def sr(key, duration=0):
    """
    Simulates pressing and holding a given key for a specified duration
    using pyautogui. Handles potential errors during key simulation.
    If duration is 0, it simulates a quick key press and release.
    """
    try:
        if duration > 0:
            pyautogui.keyDown(key)
            print(f"Simulated pressing down '{key}' for {duration} seconds.")
            wait(duration)
            pyautogui.keyUp(key)
            print(f"Simulated releasing '{key}'.")
        else:
            roblox(key) # Use the assigned pyautogui.press for quick press
            print(f"Simulated quick press of '{key}'.")
        return True
    except Exception as e:
        print(f"Error simulating key action for '{key}': {e}")
        print("Please ensure you have pyautogui installed (`pip install pyautogui`).")
        return False

def c(text):
    """
    Copies the given text to the system clipboard.
    Handles potential errors during the copy operation.
    """
    try:
        pyperclip.copy(text)
        print(f"Copied to clipboard: {text}")
        return True
    except Exception as e:
        print(f"Error copying to clipboard: {e}")
        print("Please ensure you have pyperclip installed (`pip install pyperclip`).")
        return False

def p():
    """
    Pastes text from the system clipboard by simulating the Ctrl+V shortcut.
    Handles potential errors during the paste operation.
    Returns the pasted text or None if an error occurred.
    """
    try:
        text = pyperclip.paste()
        if text is not None:
            print(f"Text retrieved from clipboard: {text}")
            # Simulate Ctrl+V to paste the text
            pyautogui.hotkey('ctrl', 'v')
            print("Simulated Ctrl+V to paste.")
        else:
            print("Clipboard is empty.")
        return text
    except Exception as e:
        print(f"Error during paste operation: {e}")
        print("Please ensure you have pyautogui and pyperclip installed.")
        return None

def sc(button, x=None, y=None, move_duration=0.75, click_delay=0.25):
    """
    Simulates a mouse click at a specific location with movement animation.
    button: 1 for left click, 2 for right click, 3 for middle click
    x, y: coordinates for the click position (optional for button-only clicks)
    move_duration: time in seconds to move to the target position (default: 0.75)
    click_delay: time in seconds to wait before clicking after reaching position (default: 0.25)
    """
    try:
        button_map = {1: 'left', 2: 'right', 3: 'middle'}
        
        if button not in button_map:
            print(f"Error: Invalid button '{button}'. Use 1 (left), 2 (right), or 3 (middle).")
            return False
        
        click_button = button_map[button]
        
        if x is not None and y is not None:
            # Move to the target position with animation
            pyautogui.moveTo(x, y, duration=move_duration)
            print(f"Moved cursor to position ({x}, {y}) in {move_duration} seconds.")
            # Wait before clicking
            wait(click_delay)
            # Perform the click
            pyautogui.click(button=click_button)
            print(f"Simulated {click_button} click at position ({x}, {y}) after {click_delay}s delay.")
        else:
            # If no coordinates provided, just click at current position with delay
            wait(click_delay)
            pyautogui.click(button=click_button)
            print(f"Simulated {click_button} click at current cursor position after {click_delay}s delay.")
        
        return True
    except Exception as e:
        print(f"Error simulating mouse click: {e}")
        print("Please ensure you have pyautogui installed (`pip install pyautogui`).")
        return False

focus_sober_window()
wait(0.2)
def bubble_gum_zen_pillar(loop_count=1, reverse=False):
    """
    Executes a predefined sequence of key presses and durations in a loop.
    :param loop_count: Number of times to repeat the sequence. Default is 1.
    :param reverse: If True, reverses directional movement keys (w<->s, a<->d, left<->right). Default is False.
    
    Note: Use Ctrl+C to interrupt execution gracefully.
    """
    # Define key mappings for reversal
    key_reverse_map = {
        w: s,
        s: w,
        a: d,
        d: a,
        left: right,
        right: left
    }
    
    sequence = [
        (b, 0.6),
        (d, 0.21),
        (e, 0.3),
        (a, 0.21),
        (w, 0.7),
        (left, 0.6),
        (w, 0.3),
        (a, 0.5),
        (w, 0.3),
        (d, 0.7),
        (a, 0.3),
        (w, 0.5),
        (d, 0.7),
        (a, 0.3),
        (s, 1.2),
        (b, 0.2)
    ]
    
    try:
        # Execute the sequence for the specified number of loops
        for loop_num in range(loop_count):
            print(f"Starting loop {loop_num + 1}/{loop_count}")
            
            # Run the original sequence
            for key, duration in sequence:
                sr(key, duration)
            
            # If reverse is True, run the reversed sequence in reverse order
            if reverse:
                print("Starting reversal")
                for key, duration in reversed(sequence):
                    reversed_key = key_reverse_map.get(key, key)
                    print(f"({key}, {duration}) - ({reversed_key}, {duration})")
                    sr(reversed_key, duration)
                    
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting gracefully...")
        return
def worms(loop_count=1):
    sequence = [
        (w, 2)
        # Reverse direction
        (s, 2)
    ]

    for _ in range(loop_count):
        for key, duration in sequence:
            sr(key, duration)
bubble_gum_zen_pillar(loop_count=2000, reverse=True)