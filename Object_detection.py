import cv2

#print(cv2.__version__)
face_cascade = cv2.CascadeClassifier('/home/vikram/Documents/haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
#img = cv2.imread('/home/vikram/Downloads/vikram.jpeg')
while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
    cv2.imshow('img', img)
    k=cv2.waitKey(30)&0xff
    if(k==27):
        break
cap.release()
