import cv2

# Task: Do the following image transformation without using any libraries (You could use opencv for exporting images only)
# 1. Flip the image horizontally, then export to a new image
# 2. Flip the image vertically, then export to a new image
# 3. Rotate the image 90 degrees, then export to a new image
# 4. Rotate the image -90 degrees, then export to a new image
# 5. Resize the image from (1600x900) to (800x450)

image = cv2.imread("Berlin.jpg")
print(image.shape)

def horizontally(image):
    height, width, channels = image.shape
    flipped_horizontal = image[:, ::-1, :]
    print("Flipped Horizontal Image Shape:", flipped_horizontal.shape)
    cv2.imwrite("Berlin_flipped_horizontal.jpg", flipped_horizontal)
horizontally(image)


def vertically(image):
    height, width, channel = image.shape
    flipped_vertically = image[::-1, :, :]
    print("Flipped Horizontal Image Shape:", flipped_vertically.shape)
    cv2.imwrite("Berlin_flipped_vertically.jpg", flipped_vertically)
vertically(image)


