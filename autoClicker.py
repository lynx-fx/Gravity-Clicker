import pyautogui
import cv2
import numpy as np
import time

template = cv2.imread("run.png")

scales = [1.0, 0.9, 0.8, 0.7]

while True:
    screenshot = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    for scale in scales:
        resized = cv2.resize(template, None, fx=scale, fy=scale)

        result = cv2.matchTemplate(screen, resized, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.75:
            x = max_loc[0] + resized.shape[1] // 2
            y = max_loc[1] + resized.shape[0] // 2

            pyautogui.click(x, y)
            print("Clicked Run")
            time.sleep(2)
            break

    time.sleep(0.2)