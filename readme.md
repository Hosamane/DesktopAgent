# Vision-Based Desktop Automation using OCR, Template Matching and GroundingDINO

## Overview

This project demonstrates intelligent desktop automation by combining Computer Vision, OCR, and UI automation techniques.

The system can visually understand desktop contents, identify applications from screenshots, launch applications through desktop interaction, fetch data from external APIs, and perform automated tasks without relying on fixed screen coordinates.

The project uses a hybrid detection pipeline consisting of:

- EasyOCR
- OpenCV Template Matching
- GroundingDINO

to improve detection reliability across different desktop environments.

---

## Features

### Desktop Screenshot Capture

- Captures screenshots of the desktop.
- Automatically switches to desktop view before analysis.

### Hybrid Desktop Icon Detection

Detects applications using a multi-stage approach:

1. OCR Detection (EasyOCR)
2. Template Matching (OpenCV)
3. GroundingDINO Object Detection

Supported applications:

- Notepad
- Chrome (template available)

### Automated Application Launching

- Identifies Notepad from desktop screenshots.
- Opens Notepad through desktop interaction.
- Eliminates dependency on hardcoded coordinates.

### API Integration

Fetches posts from:

https://jsonplaceholder.typicode.com/posts

### Automated Content Generation

Formats each post as:

Title: {title}

{body}

and enters the content automatically into Notepad.

### Automated File Saving

Saves each post as:

post_1.txt
post_2.txt
post_3.txt

...

post_10.txt

### Overwrite Handling

Detects existing files and automatically confirms overwrite operations during save.

---

## Workflow

1. Minimize all windows.
2. Capture desktop screenshot.
3. Detect Notepad icon.
4. Launch Notepad.
5. Fetch posts from JSONPlaceholder API.
6. For the first 10 posts:
   - Create a new document.
   - Type formatted content.
   - Save file as post\_{id}.txt.
   - Handle overwrite confirmation if necessary.

7. Repeat until all posts are processed.

---

## Technologies Used

### Computer Vision

- EasyOCR
- OpenCV
- GroundingDINO

### Automation

- PyAutoGUI
- PyGetWindow

### Data Processing

- Requests

### Imaging

- Pillow

### Machine Learning

- PyTorch

### Programming Language

- Python 3.x

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

cd YOUR_REPOSITORY
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install easyocr opencv-python pillow pyautogui pygetwindow requests torch
```

---

## Usage

Run:

```bash
python main.py
```

The application will:

- Show desktop.
- Detect Notepad.
- Launch Notepad.
- Fetch JSONPlaceholder posts.
- Type content automatically.
- Save posts as text files.

---

## Project Structure

````text
```text
VISIONPROJECT
│
├── main.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── hybrid_detector.py
│   ├── grounding_detector.py
│   ├── ocr_detector.py
│   ├── notepad_launcher.py
│   ├── post_saver.py
│   └── api/
│       └── jsonplaceholder.py
│
├── tests/
│   ├── test_api.py
│   ├── test_detector.py
│   ├── test_launcher.py
│   └── test_post.py
│
├── models/
│   └── groundingdino_swint_ogc.pth
│
├── templates/
│   └── notepad_icon.png
│
└── screenshots/
````

````

---

## Example Use Case

Input Source:

https://jsonplaceholder.typicode.com/posts

Generated File:

```text
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit

quia et suscipit
suscipit recusandae consequuntur expedita et cum
reprehenderit molestiae ut ut quas totam
````

Saved As:

```text
post_1.txt
```

---

## Challenges Solved

- Dynamic desktop application detection.
- Coordinate-free desktop interaction.
- Multi-stage vision-based detection.
- Automated text entry into desktop applications.
- Automated file generation from API data.
- Handling file overwrite scenarios.

---

## Future Enhancements

- Multi-monitor support.
- Vision-based popup detection.
- GroundingDINO-based button interaction.
- AI-powered desktop task execution.
- Support for additional desktop applications.
- Workflow recording and replay.

---

## Author

Hosamane Veerabhadrappa Setty

---

## License

This project is licensed under the MIT License.
