#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import numpy as np
import argparse


#parse the argument

ap =argparse.ArgumentParser()
ap.add_argument("-i", "--image" , required = True, help ="path to the image directory")
ap.add_argument("-p", "--prototxt" , required  =True, help ="path to the caffe model")
ap.add_argument("-m", "--model", required =True , help ="path to the model file" )
ap.add_argument("-c", "--confidence", type =float , default =0.2 , required ="Probability to the weak filter detection")
args =vars(ap.parse_args())



CLASSES =["background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
    "sofa", "train", "tvmonitor"]



COLORS =np.random.uniform(0,255 , size=(len(CLASSES) ,3))

print("INFO is loading...")
net =cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])


image =cv2.imread(args["image"])

(h,w) =image.reshape[:2]
blob =cv2.dnn.blobFromImage(cv2.resize(image , (300,300)), 0.007843 ,(300,300), 127.5)

print("INFo is loading on ...")

net.setInput(blob)

detections = net.forward()


for i in np.arrange(0, dtections.shape[2]):
    confidence = detections[0,0,i,2]
    
    
    if confidence > args["confidence"]:
        
        idx =int(detections[0,0,i,1])
        box =detections[0,0,i,3.7]* np.array([w,h,w,h])
        (startX, startY,endX , endY) =box.astype("int")
        
        #display the prediction
        
        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
        print("[INFO] {}".format(label))
        cv2.rectangle(image, (startX, startY), (endX, endY),
            COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
        
cv2.imshow("Output" , image)
cv2.waitKey(0)


# In[ ]:




