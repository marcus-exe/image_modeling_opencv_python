## Imports
import cv2 as cv
import numpy as np

## Read an image
original_img = cv.imread("./images/coruja.jpg")

## Define the desired width and height for the resized image
desired_width = 400
desired_height = 400

## Resize the image
resized_image = cv.resize(original_img, (desired_width, desired_height))

## Apply filter by manipulating color channels
custom_filter = np.zeros_like(resized_image)
custom_filter[:, :, 0] = 191             # Set the blue channel to 191 
custom_filter[:, :, 1] = 154             # Set the green channel to 154
custom_filter[:, :, 2] = 208             # Set the red channel to 208

## Apply the custom RGB filter to the image
custom_filter_image = cv.addWeighted(resized_image, 0.7, custom_filter, 0.3, 0)

## Alternative without the green color
purple_filter_image = np.zeros_like(resized_image)
purple_filter_image[:, :, 0] = resized_image[:, :, 0]  # Keep the blue channel as it is
purple_filter_image[:, :, 1] = 0               # Set the green channel to 0 (remove green)
purple_filter_image[:, :, 2] = resized_image[:, :, 2]  # Keep the red channel as it is

## Save Images
# Save the original and filtered images
cv.imwrite('./output/original_image.jpg', resized_image)
cv.imwrite('./output/custom_filtered_image.jpg', custom_filter_image)
cv.imwrite('./output/purple_filtered_image.jpg', purple_filter_image)

## Show the images
cv.imshow('Original Image', resized_image)
cv.imshow('Filtered Image', custom_filter_image)
cv.imshow('Purple Image', purple_filter_image)
cv.waitKey(0)
cv.destroyAllWindows()
