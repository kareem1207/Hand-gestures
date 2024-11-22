import cv2
import mediapipe as mpipe
from pyautogui import press
from time import time 

cap = cv2.VideoCapture(0)
drawing = mpipe.solutions.drawing_utils
hands = mpipe.solutions.hands
hand_obj = hands.Hands(max_num_hands=1, min_detection_confidence=0.9, min_tracking_confidence=0.9)

def count_fingers(hand_landmarks):
    fingers = []
    if hand_landmarks.landmark[mpipe.solutions.hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mpipe.solutions.hands.HandLandmark.THUMB_IP].x:
        fingers.append(1)
    else:
        fingers.append(0)

    finger_tips = [
        mpipe.solutions.hands.HandLandmark.INDEX_FINGER_TIP,
        mpipe.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP,
        mpipe.solutions.hands.HandLandmark.RING_FINGER_TIP,
        mpipe.solutions.hands.HandLandmark.PINKY_TIP,
    ]
    finger_pips = [
        mpipe.solutions.hands.HandLandmark.INDEX_FINGER_PIP,
        mpipe.solutions.hands.HandLandmark.MIDDLE_FINGER_PIP,
        mpipe.solutions.hands.HandLandmark.RING_FINGER_PIP,
        mpipe.solutions.hands.HandLandmark.PINKY_PIP,
    ]

    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:  
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)  

def perform_action(finger_count):
    actions = {
        1: 'left',
        2: 'right',
        3: 'up',
        4: 'down',
        5: 'space'
    }
    if finger_count in actions:
        print(f"Performing action: {actions[finger_count]}")
        press(actions[finger_count])

prev_count = -1
gesture_start_time = None  
repeat_delay = 2  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hand_obj.process(rgb_frame)

    if results.multi_hand_landmarks:
        for i in range(len(results.multi_hand_landmarks)):
            hand_landmarks = results.multi_hand_landmarks[i]
            drawing.draw_landmarks(frame, hand_landmarks, hands.HAND_CONNECTIONS)
            finger_count = count_fingers(hand_landmarks)

            if finger_count != prev_count:  
                gesture_start_time = time()  
                perform_action(finger_count)
                prev_count = finger_count  
            else:  
                current_time =time()
                if gesture_start_time and (current_time - gesture_start_time >= repeat_delay):
                    perform_action(finger_count)  
                    gesture_start_time = current_time  

    cv2.imshow("Hand Gesture Control", frame)

    # Exit on 'Escape' key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows() 