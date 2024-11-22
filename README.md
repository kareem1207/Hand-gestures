# Hand Gestures

## Introduction

This is code is used for controlling laptop developed using python.

## Description

The file named "main.py" is the code which runs captures the video and the gestures of done by the user which is fingers count. This code have a lot of dependencies as we are using modules for detecting the gestures.

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

## Tech stack

- python

## Requirements

- python version 3.12.7 or below
- a good code editor like vs code , anaconda , etc..
- modules like opencv , mediapipe , pyautogui

## Features

- controlling laptop using finger gestures
- customization

## Output

This is the output of the code (sorry not suited in better environment) :

[![output](output.png)](output.mp4)

## Gestures table

| Count | Gestures |
| :---: | :------: |
|   1   |   left   |
|   2   |  right   |
|   3   |   down   |
|   4   |    up    |
|   5   |  space   |

> [!Note]
> Please always check for the version as opencv , mediapipe and pyautogui is not at all integrated to python version 3.13

> [!Tip]
> It is suggested to check for the requirements by using bellow command
> pip install opencv mediapipe pyautogui or
> pip install opencv , pip install mediapipe, pip install pyautogui don't run at a time
