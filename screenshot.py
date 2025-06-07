#!/usr/bin/env python3

import subprocess
import json
import os
import glob
import sys

def get_active_window_geometry():
    """Get the geometry of the active window using hyprctl."""
    try:
        result = subprocess.run(['hyprctl', 'activewindow', '-j'], 
                              capture_output=True, text=True, check=True)
        window_data = json.loads(result.stdout)
        
        # Extract position and size
        x, y = window_data['at']
        width, height = window_data['size']
        
        return f"{x},{y} {width}x{height}"
    except (subprocess.CalledProcessError, KeyError, json.JSONDecodeError) as e:
        print(f"Error getting window geometry: {e}")
        return None

def take_screenshot():
    """Take a screenshot of the active window."""
    # Create sc directory if it doesn't exist
    os.makedirs('./sc', exist_ok=True)
    
    # Remove existing screenshots
    for file in glob.glob('./sc/*.png'):
        os.remove(file)
        print(f"Removed existing screenshot: {file}")
    
    # Get active window geometry
    geometry = get_active_window_geometry()
    if not geometry:
        print("No active window found or failed to get window geometry")
        return False
    
    # Take screenshot
    screenshot_path = './sc/active_window.png'
    try:
        subprocess.run(['grim', '-g', geometry, screenshot_path], check=True)
        print(f"Screenshot saved to {screenshot_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to take screenshot: {e}")
        return False

if __name__ == "__main__":
    if not take_screenshot():
        sys.exit(1)