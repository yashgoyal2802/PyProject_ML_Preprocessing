import numpy as np
import glob
import cv2
import os
from PIL import Image

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
    print("\n============================================================================================")
    print("EXTRACTING FEATURES")
    print("============================================================================================")
    x = input("Enter the feature separating symbol (E.g:- '_' or '-'): ")
    y = int(input("Enter the offset of the separating symbol: "))
    z = []
    for myfiles in PATH:
        z.append(myfiles.split('.')[0].split('\\')[-1].split(x)[y:])
    return z


def img_to_numpy_w_label():
    print("\n============================================================================================")
    print("IMAGES TO NUMPY ARRAY")
    print("============================================================================================")

    z = extracting_features()

    op_list = []
    final_list = []

    for myfiles in PATH:
        im = Image.open(myfiles)
        np_im = np.array(im)
        op_list.append(np_im)

    final_list = [(i, j) for i, j in zip(op_list, z)]

    return final_list


# def convert_filetype():
#     # y = glob.glob(input("Enter the path of the image/images you want to convert"))
#     y = "C:\\Users\\Varadh\\Documents\\GitHub\\PyProject_ML_Preprocessing\\Active_Workspace\\*.*"
#     y = glob.glob(y)
#
#     pngs = []
#
#     for pth in y:
#         print("=====")
#         print(pth)
#         if pth[-3:] == 'png':
#             name = pth.split('\\')[-1].split('.')[0]
#             pngs.append((name, pth))
#
#     x = int(input("Enter \n1. for .png to .jpg\n2. for .jpg to .png\n-->"))
#
#     if x == 1:
#         print("X is 1")
#         for (name, file) in pngs:
#             print("IN THE LOOP")
#             im = Image.open(file)
#
#             rgb_im = im.convert('RGB')
#
#             rgb_im.save(file.replace("png", "jpg"), quality=95)
                # for (imgname, imgpath) in pngs:
                #     im = Image.open(imgpath).convert("RGB")
                #     imgname = imgname + ".jpeg"
                #     im.save(imgname, "jpeg")
                #     print("am here")



