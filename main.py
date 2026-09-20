from PIL import Image
import numpy as np

images = Image.open("images/input.jpg")

#img to numpy array
image_array = np.array(images)
print("Origional shape = ", image_array.shape)
print("Origional datatype = ", image_array.dtype)

# Increase brightness
brighter_array = image_array-100

#value between 0 and 255
brighter_array = np.clip(brighter_array, 0, 255)

#convert numpy array back to image
brighter_image = Image.fromarray(brighter_array.astype(np.uint8))

brighter_image.save("output/brighter.jpg")
print("Brighter image Save.")