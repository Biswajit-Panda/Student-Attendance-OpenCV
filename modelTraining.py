import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import os

def train_model():
    dataPath = 'https://github.com/Biswajit-Panda/Student-Attendance-OpenCV/tree/main/img_data'
    images = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]
    # print(images)


    trainingData, lables, ids = [], [], []

    for i, files in enumerate(images):
        imagePath = dataPath + images[i]
        readImages = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        trainingData.append(np.asarray(readImages, dtype=np.uint8))
        # lables.append(i)
        Id = int(os.path.split(imagePath)[-1].split('_')[0])
        lables.append(Id)

    # print(trainingData)
    # print(lables)
    # print(ids)


    # lables = np.asarray(lables, dtype=np.int32)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(np.asarray(trainingData), np.array(lables))
    recognizer.write('model.xml')
    # print('model trained')

# train_model()

'''
faceClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # try:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            id, result = recognizer.predict(gray[y:y + h, x:x + w])

            # id = ds.sampleDict[ds.Id]


            if result < 500:
                confidence = int(100 * (1 - (result) / 300))
                confidenceString = str(confidence) + '% confidence'
                cv2.putText(frame, confidenceString, (10, 25), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)

            if confidence > 70:
                cv2.putText(frame, str(id), (x + w, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)
                cv2.imshow('face recognizer', frame)

            elif confidence < 69:
                cv2.putText(frame, 'unknown', (x + w, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
                cv2.imshow('face recognizer', frame)


        # except:
        #     cv2.putText(frame, 'face not found', (250, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)
        #     cv2.imshow('face recognizer', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
'''