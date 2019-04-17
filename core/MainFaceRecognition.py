import cv2
import os
import numpy as np
from time import sleep
import time


subjects = ["", "Shoaib","Arman","Azam"]


def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    if (len(faces) == 0):
        return None, None

    (x, y, w, h) = faces[0]

    # cv2.destroyAllWindows()

    return gray[y:y+w, x:x+h], faces[0]


def prepare_training_data(data_folder_path):

    dirs = os.listdir(data_folder_path)

    faces = []
    labels = []

    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue;

        label = int(dir_name.replace("s", ""))

        subject_dir_path = data_folder_path + "/" + dir_name

        subject_images_names = os.listdir(subject_dir_path)


        for image_name in subject_images_names:

            if image_name.startswith("."):
                continue;

            image_path = subject_dir_path + "/" + image_name

            image = cv2.imread(image_path)

            # cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            # cv2.waitKey(1)

            face, rect = detect_face(image)
            

            if face is not None:
                faces.append(face)
                labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels

print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")

print("Total faces: ", len(faces))
print("Total labels: ", len(labels))



face_recognizer = cv2.face.LBPHFaceRecognizer_create()


face_recognizer.train(faces, np.array(labels))


def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


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

	    cv2.imshow('frame',frame)
	    # print("before sleep")
	    # print("Predicting images...")
	    test_img1 = cv2.imread("my_img.png")
	    predicted_img1 = predict(test_img1)
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


def predict(test_img):
    try:
        img = test_img.copy()
        face, rect = detect_face(img)

        label, confidence = face_recognizer.predict(face)
        label_text = subjects[label]
        print('Hello ' + label_text)
        # draw_rectangle(img, rect)
        # draw_text(img, label_text, rect[0], rect[1]-5)
        print(confidence)
        if confidence < 40:
        	return img
        else:
        	pass
    except:
        takephoto()



takephoto()
