# Gravity Clicker 🚀

Gravity Clicker is a Python-based automation tool designed to detect and click a specific button (default: "Run") on your screen using image recognition. It leverages OpenCV's template matching to provide a robust solution that works even if the button's scale changes slightly.

## 🌟 Features

- **Automated Clicking**: Automatically finds and clicks the "Run" button on your screen.
- **Multi-Scale Support**: Supports multiple image scales (1.0, 0.9, 0.8, 0.7) to ensure reliable detection across different resolutions or UI scaling.
- **High Sensitivity**: Adjustable threshold for template matching to balance between accuracy and speed.
- **Efficient Loop**: Includes micro-delays to prevent high CPU usage while maintaining responsiveness.

## 🛠️ Requirements

Before running the script, ensure you have Python installed. You will also need the following libraries:

```bash
pip install pyautogui opencv-python numpy
```

## 🚀 Getting Started

1.  **Prepare the Template**: Ensure `run.png` is in the same directory as the script. This should be a clear screenshot of the button you want the script to click.
2.  **Run the Script**:
    ```bash
    python autoClicker.py
    ```
3.  **To Stop**: Press `Ctrl+C` in your terminal to terminate the process.

## ⚙️ How it Works

- The script takes a screenshot of your screen using `pyautogui`.
- It converts the screenshot into a format compatible with OpenCV (`cv2`).
- It iterates through several predefined scales of your template image.
- Using `cv2.matchTemplate`, it searches for the highest correlation between the screenshot and the template.
- If a match is found with a confidence level greater than **0.75**, it calculates the center coordinates and performs a click.
- After a successful click, it waits for **2 seconds** before resuming its search.

## ⚠️ Important Note

- This script is intended for automation and testing purposes. Ensure you are using it in accordance with the terms of service of any application you interact with.
- The script uses absolute screen coordinates. Ensure the target window is visible on your screen.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements.
