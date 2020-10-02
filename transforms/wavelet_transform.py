import numpy as np
import pywt
import cv2


def w2d(img, mode='haar', level=1):
    imArray = cv2.imread(img)
    # Datatype conversions
    # convert to grayscale
    imArray = cv2.cvtColor(imArray, cv2.COLOR_BGR2GRAY)
    # convert to float
    imArray = np.float32(imArray)
    imArray /= 255
    # compute coefficients
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    # Process Coefficients
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0

    # reconstruction
    imArray_H = pywt.waverec2(coeffs_H, mode)
    imArray_H *= 255
    imArray_H = np.uint8(imArray_H)
    # Display result
    #    numpy_vertical = np.hstack((imArray, imArray_H))
    #    numpy_vertical_concat = np.concatenate((imArray, imArray_H), axis=1)

    cv2.imshow('image', imArray_H)
    # cv2.imshow('image', numpy_vertical_concat)
    cv2.imwrite(each.replace(".jpg", "_changed2.jpg"), imArray_H)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()


image_list = ["000000000139.jpg", "000000000285.jpg", "000000000632.jpg", "000000000724.jpg"]

for each in image_list:
    w2d(each, 'db1', 2)
