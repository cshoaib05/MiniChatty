import cv2
import sys
import os


def predict(test_img):
    img = test_img.copy()
    face, rect = detect_face(img)

    label, confidence = face_recognizer.predict(face)
    label_text = subjects[label]
    print('Hello ' + label_text)
    # draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1]-5)
    # draw_text(img, confidence, rect[0], rect[2]-5)
    print(confidence)

    return img
# except:
#     pass
#     # takephoto()






def detect_face(img):
    cascPath = 'data\\haarcascade_frontalface_alt2.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        cv2.imshow('Video', frame)


        
        predicted_img1 = predict(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

        return gray[y:y+w, x:x+h], faces[0]
    video_capture.release()
    cv2.destroyAllWindows()




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

            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            # cv2.waitKey(100)

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



def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)









def main():
    while True:
        face_detect()
        

main()