import cv2
import face_recognition as fr
import os

encoders = []
names = []

def create_encoders():
    list_files = os.listdir("Pessoas")

    for file in list_files:
        im_actual = fr.load_image_file(f"Pessoas/{file}")
        im_actual = cv2.cvtColor(im_actual, cv2.COLOR_BGR2RGB)
        encoders.append(fr.face_encodings(im_actual)[0])
        names.append(os.path.splitext(file)[0])

def compare_webcam():
    video = cv2.VideoCapture(0)
    while True:
        check, img = video.read()

        img_p = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        img_rgb = cv2.cvtColor(img_p, cv2.COLOR_BGR2RGB)

        try:
            faces_location = fr.face_locations(img_rgb)[0]
        except:
            faces_location = []

        if faces_location:
            y1, x2, y2, x1 = faces_location
            y1, x2, y2, x1 = int(y1 * 4), int(x2 * 4), int(y2 * 4), int(x1 * 4)

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            encode = fr.face_encodings(img_rgb)[0]

            for id, enc in enumerate(encoders):
                compare = fr.compare_faces([encode], enc)
                if compare[0]:
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), -1)
                    cv2.putText(img, names[id], (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Video", img)
        cv2.waitKey(1)


create_encoders()
compare_webcam()