import pyscreenshot as ImageGrab
import numpy as np
import time, winsound

# Define the bounding box of the area to monitor (left, top, right, bottom)
bbox = (520, 850, 1720, 1050)  # Example values, adjust to your needs

def grab_screen(bbox):
    """Capture the screen within the given bounding box."""
    return np.array(ImageGrab.grab(bbox))

def compare_images(img1, img2):
    """Compare two images and return if they are different."""
    return not np.array_equal(img1, img2)

def main():
    # Capture the initial screen area
    previous_capture = grab_screen(bbox)
    
    while True:
        # Wait for some time before capturing the screen again
        time.sleep(0.3)  # Adjust the delay as needed

        # Capture the screen area again
        current_capture = grab_screen(bbox)
        
        # Compare the new capture with the previous one
        if compare_images(previous_capture, current_capture):
            print("New output detected!")
            winsound.Beep(1000, 200)  # Beep at 1000 Hz for 200 ms
            # Update the previous capture
            previous_capture = current_capture

if __name__ == "__main__":
    main()