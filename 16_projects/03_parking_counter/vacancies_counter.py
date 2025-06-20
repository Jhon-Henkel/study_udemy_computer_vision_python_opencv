import cv2
import pickle
import numpy as np

with open('vacancies.pkl', 'rb') as file:
    vacancies = pickle.load(file)

video = cv2.VideoCapture('video.mp4')

while True:
    check, img = video.read()
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgThreshold = cv2.adaptiveThreshold(imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)

    kernel = np.ones((5, 3), np.int8)
    imgMorph = cv2.dilate(imgMedian, kernel)

    openVacancy = 0

    for (x, y, w, h ) in vacancies:
        vacancy = imgMorph[y:y + h, x:x + w]
        count = cv2.countNonZero(vacancy)

        cv2.putText(img, str(count), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        if count < 900:
            openVacancy += 1
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.rectangle(img, (90, 0), (415, 60), (0, 255, 0), -1)
    cv2.putText(img, f'Livre: {openVacancy}/69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    cv2.imshow('Vacancies', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break