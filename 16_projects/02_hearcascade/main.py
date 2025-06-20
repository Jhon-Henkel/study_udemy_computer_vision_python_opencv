import cv2

cam = cv2.VideoCapture('video.mp4')
classifier = cv2.CascadeClassifier(r'cascades/haarcascade_fullbody.xml')

while True:
    check, img = cam.read()

    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = classifier.detectMultiScale(imgGrey, minSize=(30, 30), scaleFactor=1.5)

    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('image', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break