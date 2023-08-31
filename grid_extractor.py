# This program reads and image and extracts the sudoku grid from it using opencv and converts it to a 9x9 grid as a list of lists

import cv2
import numpy as np

# read the image
img = cv2.imread('grid_image.png')

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#display the grayscale image
cv2.imshow('gray', gray)
cv2.waitKey(0)

# apply adaptive thresholding
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 11, 2)
# display the thresholded image
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

# extract each number using contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_NONE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 1000:
        cv2.drawContours(thresh, [c], -1, (0, 255, 0), 1)

cv2.imshow('contours', thresh)
cv2.waitKey(0)

# crop the image to remove the area outside the contour
x, y, w, h = cv2.boundingRect(contours[0])
thresh = thresh[y:y + h, x:x + w]
cv2.imshow('cropped', thresh)
cv2.waitKey(0)

# resize the image to be 900x900
img = cv2.resize(thresh, (900, 900))
cv2.imshow('resized', img)
cv2.waitKey(0)

# split the image into 9x9 grid
split_img = []
rows = []
for i in range(9):
    for j in range(9):
        rows.append(img[i * 100+10:(i + 1) * 100-10, j * 100+10:(j + 1) * 100-10])
    split_img.append(rows)
    rows = []

# display the split image
for i in range(9):
    for j in range(9):
        cv2.imshow('split_img', split_img[i][j])
        cv2.waitKey(0)

# perform template matching to extract the digits
# Load digit template images
templates = []
for i in range(1, 10):  # Assuming you have digit images labeled as 0.jpg, 1.jpg, ..., 9.jpg
    template = cv2.imread(f'numbers/{i}.png', cv2.IMREAD_GRAYSCALE)
    template = cv2.resize(template, (80, 80))
    # crop the image to remove the border
    # template = template[10:70, 10:70]
    templates.append(template)

recognized_digits = []
# input_image = cv2.imread('numbers/6.png', cv2.IMREAD_GRAYSCALE)
for y in range(9):
    for x in range(9):
        input_image = split_img[y][x]
        # input_image = input_image[10:70, 10:70]
        cv2.imshow('input', input_image)
        cv2.waitKey(0)
        result = [cv2.matchTemplate(input_image, template, cv2.TM_CCOEFF_NORMED) for template in templates]
        print(result)
        # result = index of the max value in the result list
        recognized_digit = np.argmax(result) + 1
        print(recognized_digit)
        recognized_digits.append(recognized_digit)

# Print the recognized digits
print("Recognized Digits:", recognized_digits)


