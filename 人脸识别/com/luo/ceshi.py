# -*- coding: utf-8 -*-

#利用openvc 进行人脸和眼睛的识别
import cv2
#import sys  #system

#使用包里面的分类器对图片进行识别
#使用包里面的分类器对图片进行识别

#检测人脸
face_cascade = cv2.CascadeClassifier('C:/Users/luo/Desktop/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
#检测眼睛
eye_cascade = cv2.CascadeClassifier('C:/Users/luo/Desktop/opencv-3.2.0/data/haarcascades/haarcascade_eye.xml')
#输入图片路径
img_path = "C:/Users/luo/Desktop/img/3.jpg"
#读取图片
img = cv2.imread(img_path)

#将图片转换成灰白图片
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#用脸部分类器对图片进行识别
faces = face_cascade.detectMultiScale(img_gray)
#返回的 x,y坐标位置 w宽度 h高度
for(x,y,w,h) in faces:
    #用一个矩形对脸部部分进行表明
    face_area = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #再从脸部部分识别眼部
    face_gray = img_gray[y:y+h,x:x+w]
    face_color = img[y:y+h,x:x+w]
    #使用眼部检测
    eyes = eye_cascade.detectMultiScale(face_gray)
    for(ex,ey,ew,eh) in eyes:
        eye_area = cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#将结果输出
cv2.imwrite('C:/Users/luo/Desktop/img/5.png',img)