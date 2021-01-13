import cv2
import os
import csv

faceClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def faceExtractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)

    if faces is():
        return None
    for (x,y,w,h) in faces:
        # print(x,y,w,h)
        croppedFace = img[y:y+h , x:x+w]
    return croppedFace

def collectCapture(Id=1, Name='abc'):
    # Id = input("enter your id:")
    # Name = input("enter your name:")

    cap = cv2.VideoCapture(0)
    count = 0

    while True:

        ret, frame = cap.read()
        if faceExtractor(frame) is not None:
            count += 1
            face = cv2.resize(faceExtractor(frame),(250,250))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            if not os.path.exists('img_data'):
                os.makedirs('img_data')
            path = '.\\img_data\\'+ str(Id) + '_' + str(count) +'.jpg'
            # print(path)
            cv2.imwrite(path,face)

            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('face',face)

        else:
            # print('face not found')
            pass

        if cv2.waitKey(1) == 13 or count == 100 :
            break

    myDict = {'Regd No':Id,'Name':Name}

    with open('attendance.csv', "a", newline='') as f:
        writer = csv.DictWriter(f,fieldnames=['Regd No','Name'])
        writer.writerow(myDict)
    # print('data saved')

    cap.release()
    cv2.destroyAllWindows()


# collectCapture()

