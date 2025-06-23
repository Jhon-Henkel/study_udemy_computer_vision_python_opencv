import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)
hands = mp.solutions.hands

Hands = hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(imgRGB)
    handPoints = results.multi_hand_landmarks

    h, w, _ = img.shape
    pointsCapture = []

    if handPoints:
        for points in handPoints:
            mpDraw.draw_landmarks(img, points, hands.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                pointsCapture.append((cx, cy))

        fingers = [8, 12, 16, 20]
        count = 0

        if pointsCapture:
            if pointsCapture[4][0] < pointsCapture[2][0]:
                count += 1

            for x in fingers:
                if pointsCapture[x][1] < pointsCapture[x - 2][1]:
                    count += 1

        cv2.rectangle(img, (80, 10), (210, 110), (255, 0, 0), -1)
        cv2.putText(img, str(count), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)

    cv2.imshow("Image", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break