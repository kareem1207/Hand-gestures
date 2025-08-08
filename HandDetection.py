import mediapipe as mpipe
from typing import Any


class HandDetector:

    def __init__(self, cap: Any, drawing: Any, hands: Any, hand_obj: Any):
        self.cap = cap
        self.drawing = drawing
        self.hands = hands
        self.hand_obj = hand_obj

    def draw(self, frame, hand_landmarks) -> None:
        self.drawing.draw_landmarks(frame, hand_landmarks, self.hands.HAND_CONNECTIONS)

    def count_fingers(self, hand_landmarks) -> int:
        fingers :list = []

        try:
            thumb_tip : Any = mpipe.solutions.hands.HandLandmark.THUMB_TIP # pyright: ignore[reportAttributeAccessIssue]
            thumb_ip : Any = mpipe.solutions.hands.HandLandmark.THUMB_IP   # pyright: ignore[reportAttributeAccessIssue]
            fingers.append(1 if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_ip].x else 0)
        except Exception:
            fingers.append(0)

        finger_tips : list = [
            mpipe.solutions.hands.HandLandmark.INDEX_FINGER_TIP, # pyright: ignore[reportAttributeAccessIssue]
            mpipe.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP, # pyright: ignore[reportAttributeAccessIssue]
            mpipe.solutions.hands.HandLandmark.RING_FINGER_TIP, # pyright: ignore[reportAttributeAccessIssue]
            mpipe.solutions.hands.HandLandmark.PINKY_TIP, # pyright: ignore[reportAttributeAccessIssue]
        ]
        finger_pips : list = [
            mpipe.solutions.hands.HandLandmark.INDEX_FINGER_PIP, # pyright: ignore[reportAttributeAccessIssue]
            mpipe.solutions.hands.HandLandmark.MIDDLE_FINGER_PIP, # pyright: ignore[reportAttributeAccessIssue]
            mpipe.solutions.hands.HandLandmark.RING_FINGER_PIP, # pyright: ignore[reportAttributeAccessIssue]
            mpipe.solutions.hands.HandLandmark.PINKY_PIP, # pyright: ignore[reportAttributeAccessIssue]
        ]

        for tip, pip in zip(finger_tips, finger_pips):
            try:
                fingers.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y else 0)
            except Exception:
                fingers.append(0)

        return int(sum(fingers))
