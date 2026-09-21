import numpy as np


def adjust_brightness(image_array, value):
    brighter_array = image_array.astype(np.int16) + value
    brighter_array = np.clip(brighter_array, 0, 255)

    return brighter_array.astype(np.uint8)