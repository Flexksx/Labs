from PIL import Image
import numpy as np

img = np.array(Image.open('C:\\Users\\Cristi\\Documents\\GitHub\\Labs\\LabsNA\\Lab1NA\\fotka.png'))

angle = int(input("Enter the value of angle: "))
scale_height = int(input("Enter pixel height: "))
scale_width = int(input("Enter pixel width: "))

def rotation_img(angle):
    theta = np.radians(angle)
    cos = np.cos(theta)
    sin = np.sin(theta)
    rotation_matrix = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    height, width = img.shape[:2]
    new_width = int(np.round(height * np.abs(sin) + width * np.abs(cos)))
    new_height = int(np.round(width * np.abs(sin) + height * np.abs(cos)))

    cx, cy = width / 2, height / 2
    dx, dy = new_width / 2, new_height / 2
    center_matrix = np.array([[1, 0, cx], [0, 1, cy], [0, 0, 1]])
    center_matrix_inv = np.array([[1, 0, -dx], [0, 1, -dy], [0, 0, 1]])


    affine_matrix = np.dot(np.dot(center_matrix, rotation_matrix), center_matrix_inv)
    rotated_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    for y in range(new_height):
        for x in range(new_width):
            source_X, source_Y, _ = np.dot(affine_matrix, [x, y, 1]).astype(np.int)
            if 0 <= source_X < width and 0 <= source_Y < height:
                rotated_img[y, x, :] = img[source_Y, source_X, :]
    return rotated_img


def scale(im, scale_height, scale_width):
    scale_height0, scale_width0 = im.shape[:2]
    scaled_image = np.zeros((scale_height, scale_width, im.shape[2]), dtype=np.uint8)
    for r in range(scale_height):
        for c in range(scale_width):
            scaled_r = int(scale_height0 * r / scale_height)
            scaled_c = int(scale_width0 * c / scale_width)
            scaled_image[r, c] = im[scaled_r, scaled_c]
    return scaled_image

rotated_img = Image.fromarray(rotation_img(angle))
rotated_img.show()

scaled_img = scale(img, scale_height, scale_width)
Image.fromarray(np.uint8(scaled_img)).show()
