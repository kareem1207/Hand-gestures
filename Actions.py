from typing import Optional
from pyautogui import press


class Action:
    def __init__(self) -> None:
        self._mapping : dict[int, str | None] = {
            0: None,        # no action
            1: 'left',
            2: 'right',
            3: 'up',
            4: 'down',
            5: 'space',
        }

    def _resolve(self, finger_count: int) -> Optional[str]:
        return self._mapping.get(int(finger_count), None)

    def perform(self, key: str) -> None:
        press(key)

    def perform_action(self, finger_count: int) -> None:
        key = self._resolve(finger_count)
        if key:
            print(f"Performing action: {key}")
            self.perform(key)
        else:
            pass
