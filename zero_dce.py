from __future__ import annotations

import os
from functools import lru_cache
from typing import Any

import cv2
import numpy as np
import importlib
import tensorflow as tf


DEFAULT_MODEL_PATH : str = os.environ.get("ZERO_DCE_MODEL_PATH", "zero_dce.keras")


@lru_cache(maxsize=1)
def _load_model(model_path: str = DEFAULT_MODEL_PATH) -> Any:
    try:
        keras : Any | None = importlib.import_module("tensorflow.keras")
    except Exception:
        keras = None

    if not os.path.exists(model_path) or keras is None:
        return lambda x, training=False: x

    try:
        return keras.models.load_model(model_path, compile=False)
    except Exception:
        return lambda x, training=False: x


def _preprocess_bgr(frame_bgr: np.ndarray) -> np.ndarray:
    img : np.ndarray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
    return np.expand_dims(img, axis=0)


def _postprocess_rgb(batch_rgb: np.ndarray) -> np.ndarray:
    img  : np.ndarray = np.clip(batch_rgb[0], 0.0, 1.0)
    img : np.ndarray = (img * 255.0).astype(np.uint8)
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


def enhance_low_light_with_zero_dce(frame_bgr: np.ndarray) -> np.ndarray:
    model : Any = _load_model()
    batch : np.ndarray = _preprocess_bgr(frame_bgr)
    try:
        pred : Any = model(batch, training=False)
        if pred is None:
            return frame_bgr
        if isinstance(pred, tf.Tensor) and hasattr(pred, "numpy"):
            pred = pred.numpy()  # pyright: ignore[reportOptionalCall]
        elif not isinstance(pred, np.ndarray):
            pred = np.array(pred)
    except Exception:
        return frame_bgr
    return _postprocess_rgb(pred)
