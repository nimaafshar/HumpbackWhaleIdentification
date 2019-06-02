import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

for index in range(4, 5):
    # Open the image
    img = np.array(Image.open('../train/0000e88ab.jpg')).astype(np.uint8)

    # Apply gray scale
    if len(img.shape) == 3:
        gray_img = np.round(0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]).astype(np.uint8)
    else:
        gray_img = np.round(1.0 * img[:, :]).astype(np.uint8)

    # Prewitt Operator
    h, w = gray_img.shape
    # define filters
    horizontal = np.array([[-2, 0, 2], [-2, 0, 2], [-2, 0, 2]])  # s2
    vertical = np.array([[-2, -2, -2], [0, 0, 0], [2, 2, 2]])  # s1

    # define images with 0s
    newgradientImage = np.zeros((h, w))

    # offset by 1
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            horizontalGrad = (horizontal[0, 0] * gray_img[i - 1, j - 1]) + \
                             (horizontal[0, 1] * gray_img[i - 1, j]) + \
                             (horizontal[0, 2] * gray_img[i - 1, j + 1]) + \
                             (horizontal[1, 0] * gray_img[i, j - 1]) + \
                             (horizontal[1, 1] * gray_img[i, j]) + \
                             (horizontal[1, 2] * gray_img[i, j + 1]) + \
                             (horizontal[2, 0] * gray_img[i + 1, j - 1]) + \
                             (horizontal[2, 1] * gray_img[i + 1, j]) + \
                             (horizontal[2, 2] * gray_img[i + 1, j + 1])

            verticalGrad = (vertical[0, 0] * gray_img[i - 1, j - 1]) + \
                           (vertical[0, 1] * gray_img[i - 1, j]) + \
                           (vertical[0, 2] * gray_img[i - 1, j + 1]) + \
                           (vertical[1, 0] * gray_img[i, j - 1]) + \
                           (vertical[1, 1] * gray_img[i, j]) + \
                           (vertical[1, 2] * gray_img[i, j + 1]) + \
                           (vertical[2, 0] * gray_img[i + 1, j - 1]) + \
                           (vertical[2, 1] * gray_img[i + 1, j]) + \
                           (vertical[2, 2] * gray_img[i + 1, j + 1])

            # Edge Magnitude
            mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
            newgradientImage[i - 1, j - 1] = mag

    plt.figure()
    plt.title(str(index) + 'photo')
    plt.imsave(str(str(index) + '_edge.jpg'), newgradientImage, cmap='gray', format='png')
    plt.imshow(newgradientImage, cmap='gray')
    plt.show()
