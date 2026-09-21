from PIL import Image
import numpy as np

from image_tools import adjust_brightness


image = Image.open("images/input.jpg")

image_array = np.array(image)

print("Original shape:", image_array.shape)
print("Original data type:", image_array.dtype)

brightness = -50

result_array = adjust_brightness(image_array, brightness)

result_image = Image.fromarray(result_array)

result_image.save("output/brighter.jpg")

print("Brightness adjusted successfully!")