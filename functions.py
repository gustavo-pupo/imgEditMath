import numpy as np
from PIL import Image

def rotate_image(image_path, angle):
    # Load the image
    img = Image.open(image_path)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Rotate the image array
    rotated_img_array = np.rot90(img_array, k=int(angle / 90))
    
    # Convert numpy array back to image
    rotated_img = Image.fromarray(rotated_img_array)
    
    return rotated_img
# # Example usage
# image_path = "aizFanart.jpg"
# angle = 90  # Angle in degrees
# rotated_image = rotate_image(image_path, angle)
# rotated_image.show()  # Display rotated image


def flip_image(image_path, horizontal=False, vertical=False):
    # Load the image
    img = Image.open(image_path)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Flip the image array
    if horizontal:
        img_array = np.flip(img_array, axis=1)
    if vertical:
        img_array = np.flip(img_array, axis=0)
    
    # Convert numpy array back to image
    flipped_img = Image.fromarray(img_array)
    
    return flipped_img
# # Example usage
# image_path = "aizFanart.jpg"
# horizontal_flip = False
# vertical_flip = True
# flipped_image = flip_image(image_path, horizontal=horizontal_flip, vertical=vertical_flip)
# flipped_image.show()  # Display flipped image


