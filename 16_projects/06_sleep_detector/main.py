import cv2
import mediapipe as mp
import math
import time

video = cv2.VideoCapture(0)
mpFaceMesh = mp.solutions.face_mesh
faceMash = mpFaceMesh.FaceMesh()
mp_draw = mp.solutions.drawing_utils
start = 0
status = ""
timeCount = 0

while True:
    check, img = video.read()
    img = cv2.resize(img, (1000, 720))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMash.process(imgRGB)
    h, w, _ = img.shape

    if results:
        for face in results.multi_face_landmarks:
            # mp_draw.draw_landmarks(img, face, mpFaceMesh.FACEMESH_FACE_OVAL)
            eyeRightPointOneX, eyeRightPointOneY = int(face.landmark[159].x * w), int(face.landmark[159].y * h)
            eyeRightPointTwoX, eyeRightPointTwoY = int(face.landmark[145].x * w), int(face.landmark[145].y * h)

            eyeLeftPointOneX, eyeLeftPointOneY = int(face.landmark[386].x * w), int(face.landmark[386].y * h)
            eyeLeftPointTwoX, eyeLeftPointTwoY = int(face.landmark[374].x * w), int(face.landmark[374].y * h)

            cv2.circle(img, (eyeRightPointOneX, eyeRightPointOneY), 1, (255, 0, 0), 2)
            cv2.circle(img, (eyeRightPointTwoX, eyeRightPointTwoY), 1, (255, 0, 0), 2)

            cv2.circle(img, (eyeLeftPointOneX, eyeLeftPointOneY), 1, (255, 0, 0), 2)
            cv2.circle(img, (eyeLeftPointTwoX, eyeLeftPointTwoY), 1, (255, 0, 0), 2)

            rightDistance = math.hypot(eyeRightPointOneX - eyeRightPointTwoX, eyeRightPointOneY - eyeRightPointTwoY)
            leftDistance = math.hypot(eyeLeftPointOneX - eyeLeftPointTwoX, eyeLeftPointOneY - eyeLeftPointTwoY)

            if rightDistance <= 10 and leftDistance <= 10:
                cv2.putText(img, 'Sleeping', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                situation = 'closed'
                if situation != status:
                    start = time.time()
            else:
                cv2.putText(img, 'Awake', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                situation = 'open'
                timeCount = int(time.time() - start)

            if situation == 'closed':
                timeCount = int(time.time() - start)

            status = situation

            if timeCount >= 2:
                cv2.putText(img, f'You are sleeping {timeCount} seconds', (310, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break