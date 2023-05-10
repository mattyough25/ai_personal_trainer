import cv2
import numpy as np
import time
import PoseEstimationModule as pm

cap = cv2.VideoCapture("Media/BicepCurl.mp4")
detector = pm.poseDetector()
count = 0
dir = 0

while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280,720))
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
              #Right Arm
              #detector.findAngle(img, 12,14,16)
              # Left Arm
            angle = detector.findAngle(img, 11,13,15)
            per = np.interp(angle, (210,315),(0,100))
            bar = np.interp(angle, (220,315),(650,100))
            # check for dumbell curls
            color = (255,0,255)
            if per == 100:
                color = (0,255,0)
                if dir == 0:
                     count += 0.5
                     dir = 1
            if per == 0:
                 color = (0,255,0)
                 if dir == 1:
                      count += 0.5
                      dir =0
            cv2.rectangle(img, (1100,100),(1175,650),color,3)
            cv2.rectangle(img, (1100,int(bar)),(1175,650),color,cv2.FILLED)
            cv2.putText(img, f'{int(per)}%',(1100,75), cv2.FONT_HERSHEY_PLAIN,4,
                        color,4)
            
            cv2.rectangle(img, (0,450),(250,720),(0,255,0),cv2.FILLED)
            cv2.putText(img, f'{int(count)}',(45,670), cv2.FONT_HERSHEY_PLAIN,15,
                        (255,0,0),25)
        '''
        scale_percent = 50  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        imgToShow = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        '''
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break