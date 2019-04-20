import cv2




def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    if (len(faces) == 0):
        return None, None

    (x, y, w, h) = faces[0]

    # cv2.destroyAllWindows()

    return gray[y:y+w, x:x+h], faces[0]





def prephoto(test_img):
	try:
		print("")
		clf = cv2.face.LBPHFaceRecognizer_create()
		clf.read('wirteb.yml')
		img = test_img.copy()
		face, rect = detect_face(img)
		label, confidence  = clf.predict(face)
		# label, confidence = face_recognizer.predict(face)
		label_text = subjects[label]
		print('Hello ' + label_text)
		# draw_rectangle(img, rect)
		# draw_text(img, label_text, rect[0], rect[1]-5)
		print(confidence)
		if confidence < 40:
			return label
		else:
			print("IN ELSE")
	except:
		# takephoto()
		pass




def takephoto():
	try:
	    face_cascade= cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml')
	    cap = cv2.VideoCapture(0)
	    ret,frame = cap.read()
	    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	    faces= face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
	    for(x,y,w,h) in faces:
	        # print(x,y,w,h)
	        roi_gray = gray[y:y+h, x: x+w]
	        # img_item = 'my_img.png'
	        cv2.imwrite('my_img.png',roi_gray)

	    # cv2.imshow('frame',frame)
	    # print("before sleep")
	    # print("Predicting images...")
	    test_img1 = cv2.imread("my_img.png")
	    predicted_img1 = prephoto(test_img1)
	    # cv2.imshow("Test1", cv2.resize(predicted_img1, (400, 500)))
	    # time.sleep(5)
	    # cv2.waitKey(0)
	    # print("aftersleep")
	    # if cv2.waitKey(20) & 0xFF == ord('q'):
	    #     break

	    cap.release()
	    cv2.destroyAllWindows()
	except:
		pass



