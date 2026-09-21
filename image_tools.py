import numpy as np
from PIL import Image

def adjust_brightness(image_array, value):
    brighter_array = image_array.astype(np.int16) + value
    brighter_array = np.clip(brighter_array, 0, 255)

    return brighter_array.astype(np.uint8)

def graysacale_image(image_array):
    grayscale_array = np.mean(image_array, axis=2)

    return grayscale_array.astype(np.uint8)

def resize_image(image_array, width, height):
    image = Image.fromarray(image_array)

    resized_image = image.resize((width, height))

    return np.array(resized_image)