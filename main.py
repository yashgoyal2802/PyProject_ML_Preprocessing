import numpy as np
import glob
import cv2
import os

# PATH = input("Enter the path to your files: ")
PATH = glob.glob("C:\\Users\\Varadh\\Documents\\GitHub\\PyProject_ML_Preprocessing\\Active_Workspace\\*.jpg")
# for myfiles in PATH:
#     print(myfiles)


def img_resize():
    print("\n============================================================================================")
    print("RESIZING IMAGES")
    print("============================================================================================")
    temp_width = int(input("Enter the width to resize the image to:     "))
    temp_height = int(input("Enter the height to resize the image to:   "))

    for my_img in PATH:
        img = cv2.imread(my_img)
        print('\nOriginal Dimensions:  ', img.shape)
        resized_img = cv2.resize(img, (temp_width, temp_height))
        print('Resized Dimensions:   ', resized_img.shape)
        cv2.imwrite(my_img, resized_img)

    print("\n============================================================================================")
    print("Completed Resizing Images")
    print("============================================================================================\n")

def img_to_grey():
    print("\n============================================================================================")
    print("GREYSCALLING IMAGES")
    print("============================================================================================")

    for my_img in PATH:
        img = cv2.imread(my_img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(my_img, gray)
    print("\n============================================================================================")
    print("Completed Greyscalling Images")
    print("============================================================================================\n")


def extracting_features():
    pass

def convert_filetype():
    pass

def img_to_numpy_w_label():
    pass
