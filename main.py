from typing import Any
import cv2
import mediapipe as mpipe
from time import time
import numpy as np

from Actions import Action
from HandDetection import HandDetector
from zero_dce import enhance_low_light_with_zero_dce


def main() -> None:
    cap: Any = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    drawing: Any = mpipe.solutions.drawing_utils # type: ignore
    hands: Any = mpipe.solutions.hands # pyright: ignore[reportAttributeAccessIssue]
    hand_obj: Any = hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    detector: HandDetector = HandDetector(cap=cap, drawing=drawing, hands=hands, hand_obj=hand_obj)
    actions: Action = Action()

    prev_count: int = -1
    gesture_start_time: float | None = None # type: ignore
    repeat_delay: float = 2.0  # seconds

    try:
        while True:
            ret , frame  = cap.read()
            if not ret:
                print("Warning: Frame grab failed; exiting loop.")
                break

            enhanced_frame : np.ndarray = enhance_low_light_with_zero_dce(frame)

            frame : np.ndarray = cv2.flip(enhanced_frame, 1)
            rgb_frame : np.ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results : Any = hand_obj.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    detector.draw(frame, hand_landmarks)
                    finger_count : int = detector.count_fingers(hand_landmarks)

                    if finger_count != prev_count:
                        gesture_start_time: float = time()
                        actions.perform_action(finger_count)
                        prev_count : int = finger_count
                    else:
                        current_time: float = time()
                        if gesture_start_time and (current_time - gesture_start_time >= repeat_delay):
                            actions.perform_action(finger_count)
                            gesture_start_time : float = current_time

            cv2.imshow("Hand Gesture Control", frame)

            # Exit on 'Escape' key
            if cv2.waitKey(1) & 0xFF == 27:
                break
    finally:
        try:
            hand_obj.close()
        except Exception:
            print(Exception)
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
