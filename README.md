# Image Processing and Recognition Basics

## Description

The goal is to write a computer vision program to easily evaluate answers of students by scanning their response OMR sheets. This is to help professors evaluate answer sheets comfortably and effectively. In total, there are three tasks to perform. One is, to use scanned image file to generate student's responses and evaluate their answers depending on the correct answers. To perform this task, we need to first inject correct answers into the response sheet before giving them to students to record their answers. So, a blank-form is injected with correct answers in a manner that student's couldn't decode the answers. After injecting these correct answers, and getting the responses from students, next is to extract the correct answers and decode it from these scanned response sheets that are injected with correct answers. After extracting the correct answers, we should evaluate the grades of students, by checking their responses with respect to the corect answers. These tasks are divided into three programs.


## Code

1. Program that utilizes a scanned image file to generate Student's responses (grade.py)
2. Program to inject correct answers into the response sheet(inject.py)
3. Program to extract accurate answers from the injected response sheet (extract.py)


### grade.py

#### In grade.py file, tasks performed are:
1. Firstly, we are cropping the image till the option values. To access the option blocks easily
2. Next, we are converting the question paper image to grayscale to maintain consistency
3. And we are inverting the image, so that our boxes are white and the background is black
4. Drew lines vertically and horizontally on pixels, to locate the options blocks perfectly. The idea here is that the lines lying on the top or bottom of the boxes will correspond to a sum of pixel intensity greater than a threshold in comparison to other rows as we scan through the document
5. Next, we are using a kind of suppression where if we get a line, we are taking the next line, only after it increases after a decrease in the value of the sum of the pixel intensities.
6. Next, we are segmenting all the boxes and finding the sum of pixel values for each box and if the sum is >400(20x20), we are counting it as an answer.
For example, if the student opts 'AB' depending on the sum of pixel intensities we are able to recognise it and store the answer as 'AB'
7. For the case, where there's something written on the left side of the options, we are checking for the pixel intensity and if there is high pixel intensity towards leftside of the options, we are considering to add 'x' on the end of the recognised answer option

To run the grade.py python code, use:
```
python3 grade.py ./test_images/a-3.jpg output.txt
```


### inject.py

#### In inject.py file, tasks performed are:
1. Converted the blank-form image to gray scale
2. Created a dictionary to save the answer options probabilities with a difference of 2 (thickness of the bars in the barcode)
3. Next, we are getting the correct answers from the provided ground truth file
4. The answers that are given in the format of numbers followed by alphabets, we are extracting the alphabet options excluding the question numbers. While extracting these options, if there are any extra spacings we are stripping them off
5. Next, converted the image as numpy array to access the x and y coordinates for performing inject operation
6. Now, we are injecting barcode format of answers on top left corner. For that, we are inserting zeros in the converted numpy array till the answer option values to match the count of zeros to stride values and I'm removing the noise in the middle by making the space as white between options (if the option is A then a bar of thickness 2px was inserted)
7. To detect different options we are inserting white (255 as pixels) after that particular number of zero's of thickness 3px
8. In the end, we are injecting this barcode and saving it into inject.jpg

#### Problems faced while creating the logic

I first tried to embed the answers as watermarks near the answers. This was an issue as the answers were supposed to hidden in a form which couldn't be read by the students. Second approach was to put in a pixel denisty based marking scheme where each option was a particular pixel density meaning A would be 1, B would be 8 and so on. The problem was to differentiate betweeen each pixel for the answers, i.e. 85 lines/dots would be there. But the problem came when there was the difference between each option was only 8 pixels so we can make 36 options within 0 and 255. But the issue was when we saved the image and read it again (similar to printing and scanning), the pixel values changed so I changed it to make a barcode of the same values but the thickness of the bars would vary based on the options. This was more reliable because even if the pixel values changed when we converted it into grayscale or binary everything was either 0 or 255 so the change in pixel values did not matter. This was finally decided as the method of encoding the answers.

To run the inject.py python code, use:
```
python3 inject.py ./test_images/blank_form.jpg ./test_images/a-3_groundtruth.txt injected.jpg
```


### extract.py

#### In extract.py file, tasks performed are:
1. Converted inject.jgp to gray scale
2. Created a dictionary to save the answer options probabilities with stride 2
3. To reduce the noise reduction that would get injected while scanning the answer sheet, we are making the pixel values with greater than or equal to 230 as white i.e., 255 and for less than or equal to 50 as 0
4. We are getting the key values into count from the number of zeros of ans_arr. The number of zero pixels would tell the option value. So, depending on the count value we get the related answer option
5. As per the count value we get the alphabet option from ans_dict and appended this to our final ans_key
6. In Final step, I added these extracted answer values to output.txt file

To run the extract.py python code, use:
```
python3 extract.py injected.jpg output.txt
```
