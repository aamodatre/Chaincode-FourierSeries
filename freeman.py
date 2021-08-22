"""Script to run the image processing"""

"""Built-in Imports"""
import sys, os, subprocess

""" Library Imports"""
import cv2 as cv
# from PIL import Image # alternative to using OpenCV
import numpy as np
import matplotlib.pyplot as plt

"""Script Imports"""
import chaincode as cc

def i2npy(imgpath):
    """ Importing image and store contour as numpy array """
    
    img = cv.imread(imgpath, 0)
    cv.imshow("image.png", img)
    cv.waitKey(0) 
    cv.destroyAllWindows()
    img = cv.bitwise_not(img)
    cv.imshow("image.png", img)
    cv.waitKey(0) 
    cv.destroyAllWindows()

    # Detecting contours in image.
    contours, _= cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    # Alternatively - when converting to a binary image
    # _, threshold = cv.threshold(img, 110, 255, cv.THRESH_BINARY)
    # contours, _= cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    return img, np.array(contours[0], dtype = np.int64).sum(axis = 1)

def sqplot(x,y):
    """ Equal axis plot - Press Q to Close"""
    fig = plt.figure(figsize = (10,10))
    # ax1, ax2 = fig.subplots(1,2)
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,4)
    ax1.plot(x,y, color = "black")
    ax1.set_title("Contour Determined")
    ax2.scatter(x,y, color = "black")
    ax2.set_title("Sampling Density")
    plt.show()
    plt.close()

if __name__ == "__main__":
    img, contour = i2npy("./Images/circle.png")
    x = contour[:,0]
    np.append(x,x[0])
    y = contour[:,1]
    np.append(y,y[0])
    sqplot(x,y)
    circlechain = cc.generateChainCode(contour)

# Next Steps:
# 1. Determine the Fourier Coefficients.
# 2. 