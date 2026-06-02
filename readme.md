# Desktop Automation using OCR

## Overview

This project automates desktop interactions by combining screenshot capture, Optical Character Recognition (OCR), and mouse automation.

The application can:

* Minimize all open windows and switch to the desktop.
* Capture a screenshot of the desktop.
* Detect text on the screen using EasyOCR.
* Locate specific applications or icons by their text labels.
* Identify the coordinates of detected text.
* Automatically move the mouse and perform clicks or double-clicks on the detected location.

## Features

* Desktop screenshot capture using Pillow.
* OCR-based text detection with EasyOCR.
* Automatic coordinate extraction from detected text.
* Mouse automation using PyAutoGUI.
* OpenCV-based image annotation for debugging and visualization.
* Dynamic application launching through text recognition.

## Technologies Used

* Python 3.x
* EasyOCR
* OpenCV
* Pillow
* PyAutoGUI

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install easyocr opencv-python pillow pyautogui
```

## Usage

Run the script:

```bash
python ocr.py
```

The script will:

1. Minimize all windows.
2. Capture the desktop screenshot.
3. Search for the target text (e.g., "Notepad").
4. Determine the text coordinates.
5. Double-click the detected location.

## Example Workflow

* Desktop contains an icon named "Notepad".
* OCR detects the text label.
* Bounding box coordinates are extracted.
* The center of the bounding box is calculated.
* The script performs a double-click on the icon.

## Project Structure

```text
.
├── ocr.py
├── screen.png
├── result.png
├── requirements.txt
└── README.md
```

## Future Enhancements

* Template matching for icon recognition.
* Multi-monitor support.
* Voice-controlled automation.
* AI-powered desktop navigation.
* Workflow automation for common desktop tasks.

## Author

Hosamane Veerabhadrappa Setty

## License

This project is licensed under the MIT License.
