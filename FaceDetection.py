# import cv2 # import openCV

# alg = 'haarcascade_frontalface_default.xml'  # accessed the model file

# cascade = cv2.CascadeClassifier(alg) # loading the model with cv2

# cam = cv2.VideoCapture(0) # initialization camera

# while True:
    
#     _,img = cam.read() # read the frame from the camera
    
#     grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # converting color into gray scale image

#     face = cascade.detectMultiScale(grayImg) # get coordinates of face

#     for (x, y, w, h) in face: # segregating x,y,w,h
        
#         cv2.rectangle(img, (x, y), (x + w, y + h),(0,255,0),2) # draw the retangle

#     cv2.imshow("FaceDetect",img)

#     key = cv2.waitKey(1)

#     if key == 81 or key == 113 :
#         break

# cam.release()
# cv2.destroyAllWindows()
        

    

 

import cv2

alg = 'C://Users//anand//Desktop//dfg//haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 2)
    cv2.imshow('FaceDetect', img)

    if cv2.waitKey(1) & 0xFF in [81, 113]:  # Q or q to quit
        break

cam.release()
cv2.destroyAllWindows()


