import cv2
import numpy as np
img_item = []
face_cascade= cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
i=0
while(True):
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces= face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
	for(x,y,w,h) in faces:
		j = str(i)
		print(x,y,w,h)
		if(i>500):
			break
		roi_gray = gray[y:y+h, x: x+w]
		img_item.append('my_img'+j+'.png')
		cv2.imwrite(img_item[i],roi_gray)
		i= i+1

	cv2.imshow('frame',frame)
	if(i>500):
			break
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()