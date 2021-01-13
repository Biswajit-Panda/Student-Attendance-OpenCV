import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import os
import pandas as pd
from datetime import date


def take_attendance():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('model.xml')

    faceClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    present = []

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            # try:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                Id, result = recognizer.predict(gray[y:y + h, x:x + w])

                if result < 500:
                    confidence = int(100 * (1 - (result) / 300))
                    confidenceString = str(confidence) + '% confidence'
                    cv2.putText(frame, confidenceString, (10, 25), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)

                if confidence > 70:
                    cv2.putText(frame, str(Id), (x + w, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)
                    cv2.imshow('face recognizer', frame)
                    if Id not in present:
                        present.append(Id)

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

    # updating the attendance sheet
    df = pd.read_csv('attendance.csv')
    today = date.today().strftime('%d/%m/%Y')

    df[today] = ['A']*df.shape[0]

    for i in present:
        df.loc[(df['RegdNo'] == i), today]='P'

    df.to_csv('attendance.csv',index=False)
    print('attendance complete...')
    
# take_attendance()