import cv2

video_capture = cv2.VideoCapture(0)

sample = 1

while True:
    check, img = video_capture.read()

    if cv2.waitKey(1) & 0xFF == ord('s'):
        imgR = cv2.resize(img, (32, 32))
        cv2.imshow(f'images/1/im{sample}.jpg', imgR)
        print(f'Imagem salva {sample}')
        sample += 1

    cv2.imshow('Video', img)
    cv2.waitKey(1)
