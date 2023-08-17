from PIL import Image, ImageChops, ImageDraw
from PIL import ImageFilter
import sys
import random
import numpy as np

if __name__ == '__main__':
    # Load an image 
    im = Image.open(sys.argv[1])

    im = im.crop((90, 620, 1470, 2080))
    gray_im = im.convert('L')
    gray_im_inv = ImageChops.invert(gray_im)
    gray_im_inv = gray_im_inv.convert('1')
    line_x = []
    line_y = []
    n_rows = gray_im_inv.height
    n_cols = gray_im_inv.width
    first = True
    draw = ImageDraw.Draw(gray_im_inv)
    sum_pixel_r = []
    sum_pixel_c = []

    for j in range(n_rows):
        pixel_sum_r = 0
        for i in range(n_cols):
            pixel_sum_r += gray_im_inv.getpixel((i,j))
        sum_pixel_r.append(pixel_sum_r)
        if pixel_sum_r >= 46000 and first == True: #and pixel_sum_c <= 200000 # and pixel_sum_r <= :(6000,26000)
            line_y.append(j)
            draw.line(((0, j),(gray_im_inv.width, j)), fill=255, width = 1)
            first = False
        if pixel_sum_r <= 21000:
            first = True
    first = True
    for i in range(n_cols):
        pixel_sum_c = 0
        for j in range(n_rows):
            pixel_sum_c += gray_im_inv.getpixel((i,j))
        sum_pixel_c.append(pixel_sum_c)
        if pixel_sum_c >= 170000 and first == True: #170000#and pixel_sum_c <= 200000 # and pixel_sum_r <= :(6000,26000)
            line_x.append(i)
            draw.line(((i, 0),(i, gray_im_inv.height)), fill=255, width = 1)
            first = False
        if pixel_sum_c <= 100000: #100000
            first = True

    gray_im_inv.save("output.jpg")

gray_im_inv = np.array(gray_im_inv)
answers = []
line_x_1 = []
line_x_2 = []
line_x_3 = []

for x in line_x:
    if x < 480:
        line_x_1.append(x)
    elif x > 480 and x < 960:
        line_x_2.append(x)
    else:
        line_x_3.append(x)
#for qs. 1 -> 29
for i in range(len(line_y)-1):
    answer = []
    if (line_y[i+1] - line_y[i]) >= 30:
        count = 0
        for j in range(len(line_x_1)-1):
            if (line_x_1[j+1]- line_x_1[j]) >= 30:
                box = gray_im_inv[line_y[i]:line_y[i+1], line_x_1[j]:line_x_1[j+1]]
                count += 1
                pixel_sum = np.sum(box)
                if pixel_sum > 400:
                    answer.append(count)
        answers.append(answer)


# #for qs. 30 -> 58
for i in range(len(line_y)-1):
    answer = []
    if (line_y[i+1] - line_y[i]) >= 30:
        count = 0
        for j in range(len(line_x_2)-1):
            if (line_x_2[j+1]- line_x_2[j]) >= 30:
                box = gray_im_inv[line_y[i]:line_y[i+1], line_x_2[j]:line_x_2[j+1]]
                count += 1
                pixel_sum = np.sum(box)
                if pixel_sum > 400:
                    answer.append(count)
        answers.append(answer)
       
# for qs. 59 -> 85
for i in range(len(line_y)-4):
    answer = []
    if (line_y[i+1] - line_y[i]) >= 30:
        count = 0
        for j in range(len(line_x_1)-1):
            if (line_x_1[j+1]- line_x_1[j]) >= 30:
                box = gray_im_inv[line_y[i]:line_y[i+1], line_x_1[j]:line_x_1[j+1]]
                count += 1
                pixel_sum = np.sum(box)
                if pixel_sum > 400:
                    answer.append(count)
        answers.append(answer)

mapping = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'}
with open(sys.argv[2], 'w') as f:
    for line, answer in enumerate(answers):
        options = ""
        for i in answer:
            if i > 5:
                continue
            options += mapping[i]
        f.write(f"{line+1} {options}")
        f.write("\n")              
