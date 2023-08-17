#!/usr/bin/env python
# coding: utf-8

from PIL import Image, ImageOps, ImageFilter
import sys
import random
import numpy as np



#Converted inject.jpeg to gray.

img = Image.open(sys.argv[1])
img = ImageOps.grayscale(img)
image = np.array(img)


#Saved answer options probabilities with stride 2.
ans_dict = {
 2: 'A',
 4: 'B',
 6: 'C',
 8: 'D',
 10: 'E',
 12: 'AB',
 14: 'AC',
 16: 'AD',
 18: 'AE',
 20: 'BC',
 22: 'BD',
 24: 'BE',
 26: 'CD',
 28: 'CE',
 30: 'DE',
 32: 'ABC',
 34: 'ABD',
 36: 'ABE',
 38: 'ACD',
 40: 'ACE',
 42: 'ADE',
 44: 'BCD',
 46: 'BCE',
 48: 'BDE',
 50: 'CDE',
 52: 'ABCD',
 54: 'ABCE',
 56: 'ABDE',
 58: 'ACDE',
 60: 'BCDE',
 62: 'ABCDE'}

ans_key = []


#Making less than or equal to 50 pixel values as 0(black)
#And greater than or equal to 230 pixel values as 255(white)
for i in range(50, 110):
    for j in range(len(image[i])):
        if image[i][j] <=50:
            image[i][j] = 0
        if image[i][j] >=230:
            image[i][j] = 255


ans_arr = image[109][55:]


# Getting the key values into count from the number of zeros of ans_arr
#As per the count value we get the alphabet option from ans_dict and appended this to our final ans_key
count = 0
for k in range(55, image.shape[1]):
    one_count, zero_count = 0, 0
    for j in range(55, 110):
        if image[j][k] == 0:
            zero_count += 1
        elif image[j][k] == 255:
            one_count += 1
    final_value = 0 if zero_count > one_count else 255
    
    if final_value == 0:
        count += 1
    elif final_value == 255:
        if count != 0:
            ans_key.append(ans_dict[count])
            count = 0


#Adding answer values to output.txt

with open(sys.argv[2], "w") as f:
    for i in range(0, 85):
        f.write(str(i+1) + " " + str(ans_key[i]) + "\n")





