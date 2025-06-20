import cv2
import pickle

img = cv2.imread('estacionamento.png')

vacancies = []

for x in range(69):
    vacancy = cv2.selectROI('Vagas', img, False)
    cv2.destroyWindow('Vagas')
    vacancies.append(vacancy)

    for (x, y, w, h) in vacancies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

with open('vacancies.pkl', 'wb') as file:
    pickle.dump(vacancies, file)