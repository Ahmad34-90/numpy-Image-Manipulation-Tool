from PIL import Image
import numpy as np

from image_tools import adjust_brightness, graysacale_image ,resize_image


image = Image.open("images/input.jpg")

image_array = np.array(image)

print("Original shape:", image_array.shape)
print("Original data type:", image_array.dtype)

# brightness
brightness = -50

result_array = adjust_brightness(image_array, brightness)

result_image = Image.fromarray(result_array)

result_image.save("output/brighter.jpg")

print("Brightness adjusted successfully!")

#grayscale 

gray_image = graysacale_image(image_array)
gray_image = Image.fromarray(gray_image)

gray_image.save("output/graysacleImag.jpg")

#resize Image

# Resize
resized_array = resize_image(image_array, 500, 360)

resized_image = Image.fromarray(resized_array)

resized_image.save("output/resized.jpg")

print("Resized image saved!")
print("New shape:", resized_array.shape)