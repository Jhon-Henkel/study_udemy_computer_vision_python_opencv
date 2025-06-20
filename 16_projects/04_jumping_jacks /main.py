import cv2
import mediapipe as mp
import math

from sympy import false

video = cv2.VideoCapture('video.mp4')
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils
count = 0
check = True

while True:
    _, img = video.read()
    video_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(video_rgb)
    points = results.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    h, w, _ = img.shape

    if points:
        feetRightY = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y * h)
        feetRightX = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x * w)

        feetLeftY = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y * h)
        feetLeftX = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x * w)

        handRightY = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y * h)
        handRightX = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x * w)

        handLeftY = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y * h)
        handLeftX = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x * w)

        handDistance = math.hypot(handRightX - handLeftX, handRightY - handLeftY)
        feetDistance = math.hypot(feetRightX - feetLeftX, feetRightY - feetLeftY)

        if check == True and handDistance <= 150 and feetDistance >= 150:
            count += 1
            check = False

        if handDistance > 150 and feetDistance < 150:
            check = True

        text = f'Contagem: {count}'
        cv2.putText(img, text, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

    cv2.imshow('Video', img)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break