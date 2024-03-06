import cv2

# Load the image
image = cv2.imread("Berlin.jpg")
print("Original Image Shape:", image.shape)

def rotate_90_degrees(image):
    rotated_90 = cv2.transpose(image)
    rotated_90 = cv2.flip(rotated_90, 1)
    print("Rotated 90 Degrees Image Shape:", rotated_90.shape)
    cv2.imwrite("Berlin_rotated_90_degrees.jpg", rotated_90)

def rotate_minus_90_degrees(image):
    rotated_minus_90 = cv2.transpose(image)
    rotated_minus_90 = cv2.flip(rotated_minus_90, 0)
    print("Rotated -90 Degrees Image Shape:", rotated_minus_90.shape)
    cv2.imwrite("Berlin_rotated_minus_90_degrees.jpg", rotated_minus_90)

def resize_image(image, new_size):
    resized_image = cv2.resize(image, new_size)
    print("Resized Image Shape:", resized_image.shape)
    cv2.imwrite("Berlin_resized.jpg", resized_image)

# Rotate 90 degrees
rotate_90_degrees(image)

# Rotate -90 degrees
rotate_minus_90_degrees(image)

# Resize image
new_size = (800, 450)
resize_image(image, new_size)
