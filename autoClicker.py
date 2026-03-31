import pyautogui
import cv2
import numpy as np
import time
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load templates for run and retry buttons
templates = {
    "run": cv2.imread(os.path.join(script_dir, "run.png")),
    "allow": cv2.imread(os.path.join(script_dir, "allow.png")),
    "retry": cv2.imread(os.path.join(script_dir, "retry.png")),
    "accept": cv2.imread(os.path.join(script_dir, "accept.png"))
}

scales = [1.0, 0.9, 0.8, 0.7]

while True:
    screenshot = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    clicked = False
    for button_name, template in templates.items():
        for scale in scales:
            resized = cv2.resize(template, None, fx=scale, fy=scale)

            result = cv2.matchTemplate(screen, resized, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val > 0.75:
                x = max_loc[0] + resized.shape[1] // 2
                y = max_loc[1] + resized.shape[0] // 2

                pyautogui.click(x, y)
                print(f"Clicked {button_name.capitalize()}")
                clicked = True
                break
        if clicked:
            break

    if clicked:
        time.sleep(2)
    else:
        time.sleep(0.2)