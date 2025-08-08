# Hand Gestures

## Introduction

This is code is used for controlling laptop developed using python.

## Description

The file named "main.py" is the code which runs captures the video and the gestures of done by the user which is fingers count. This code have a lot of dependencies as we are using modules for detecting the gestures.

## Installation and Usage

### Clone the Repository

git clone <repository-url>
cd <repository-folder>

### Install dependencies

pip install opencv-python mediapipe pyautogui

### Run the Script

python main.py

### Opencv

The use of opencv library in this code is to capture the video from the camera of the computer and show what it is seeing using "cv2.imshow()" and capturing video using "cv2.VideoCapture(value)".

- value:0 = gets the video data from the primary camera.
- value:1 = gets the video data from the secondary camera.
- value:-1 = gets the video data from the nearest camera.

### Mediapipe

The use of Mediapipe library in this code mandatory as it detects the hand motion , it is basically developed using non regression concept and it is flexible as we can use that for many functionality like face detection , motion detection etc..

in this code we are detecting the code based on the confidence levels of the computer that the hand in a video is really hand , it has been set to 90%(0.9) and can be changed to any value.

### Pyautogui

The use of Pyautogui library in this code is used to perform operations like clicking a certain key board button

### About Zero‑DCE (night mode)

- Zero‑DCE (Zero‑Reference Deep Curve Estimation) enhances low‑light frames in real time.
- The app loads a Keras model from `ZERO_DCE_MODEL_PATH` (env var) or `zero_dce.keras` in the project root.
- If a model isn’t present, the app still runs but without enhancement.

## Tech stack

- Python 3.10 (recommended) or 3.11
- OpenCV, MediaPipe, PyAutoGUI, NumPy
- TensorFlow/Keras for Zero‑DCE (night mode)

## Requirements

- Python 3.10–3.11
- A code editor like VS Code, Anaconda Navigator, etc.
- Packages: opencv‑python, mediapipe, pyautogui, numpy, tensorflow
- TensorFlow powers the Zero‑DCE low‑light enhancement used for “night mode”.

## Features

- Control laptop using finger gestures
- Night mode: Zero‑DCE low‑light enhancement for low‑light scenes
- Customization (adjust key mappings and thresholds)

## Output

This is the output of the code (sorry not suited in better environment) :

[![output](output.png)](output.mp4)

## Gestures table

| Count | Gestures |
| :---: | :------: |
|   1   |   left   |
|   2   |  right   |
|   3   |    up    |
|   4   |   down   |
|   5   |  space   |

> [!Note]
> Use Python 3.10 or 3.11 for best compatibility. OpenCV, MediaPipe, and PyAutoGUI may not have stable wheels for Python 3.12/3.13 on Windows yet.

> [!Tip]
> Install dependencies via the provided requirements file:
> `pip install -r requirements.txt`
>
> Or individually:
> `pip install opencv-python mediapipe pyautogui numpy tensorflow`
>
> To use night mode, provide a model file at `zero_dce.keras` or set `ZERO_DCE_MODEL_PATH` to your model path.
