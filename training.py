#!/usr/bin/env python3

import os
import sys
import pyautogui

def find_image_in_target(find_image, target_image):
    """Find a specific training image within a target screenshot."""
    training_image_path = f"./training_image/{find_image}.png"
    screenshot_path = f"./sc/{target_image}.png"
    
    # Check if both files exist
    if not os.path.exists(training_image_path):
        print(f"Training image not found: {training_image_path}")
        return None
    
    if not os.path.exists(screenshot_path):
        print(f"Screenshot not found: {screenshot_path}")
        return None
    
    print(f"Searching for '{find_image}' in '{target_image}'...")
    
    try:
        # Use pyautogui to locate the training image in the screenshot
        location = pyautogui.locate(training_image_path, screenshot_path, confidence=0.8)
        
        if location:
            center = pyautogui.center(location)
            return {
                'find_image': find_image,
                'target_image': target_image,
                'left': location.left,
                'top': location.top,
                'width': location.width,
                'height': location.height,
                'center_x': center.x,
                'center_y': center.y
            }
        else:
            return None
            
    except pyautogui.ImageNotFoundException:
        return None
    except Exception as e:
        print(f"Error detecting '{find_image}' in '{target_image}': {e}")
        return None

def detect_images_from_list(image_pairs):
    """Detect images sequentially from a list of (find_image, target_image) pairs."""
    results = []
    
    for find_image, target_image in image_pairs:
        print(f"\n--- Checking for '{find_image}' in '{target_image}' ---")
        result = find_image_in_target(find_image, target_image)
        
        if result:
            print(f"✓ {find_image} was found in {target_image}!")
            print(f"  Position: x={result['left']}, y={result['top']}")
            print(f"  Center: x={result['center_x']}, y={result['center_y']}")
            results.append(result)
        else:
            print(f"✗ {find_image} was not found in {target_image}")
    
    return results

def main():
    # Define your list of (find_image, target_image) pairs
    my_list = [
        ("lucky", "base"),
        ("mythic", "base"),
    ]
    
    print("Starting sequential image detection...")
    print("Search pairs:")
    for find_img, target_img in my_list:
        print(f"  • Looking for '{find_img}' in '{target_img}'")
    
    # Detect all images in the list
    found_images = detect_images_from_list(my_list)
    
    # Summary
    print("\n" + "="*50)
    print("DETECTION SUMMARY")
    print("="*50)
    
    if found_images:
        print(f"Found {len(found_images)} image(s):")
        for result in found_images:
            print(f"  • {result['find_image']} found in {result['target_image']} at ({result['center_x']}, {result['center_y']})")
    else:
        print("No images were found")
    
    print(f"Total searched: {len(my_list)}")
    print(f"Total found: {len(found_images)}")

if __name__ == "__main__":
    main()