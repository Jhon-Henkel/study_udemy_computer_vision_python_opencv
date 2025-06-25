import pytesseract as pt
import cv2

img = cv2.imread('imgteste.JPG')

# print(pt.pytesseract.image_to_string(img, lang='por'))

boxes = pt.pytesseract.image_to_boxes(img, lang='por')
imgHeight, imgWidth, _ = img.shape

for box in boxes.splitlines():
    box = box.split(' ')
    letter, x, y, w, h = box[0], int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, imgHeight - y), (w, imgHeight - h), (0, 0, 255), 2)
    cv2.putText(img, letter, (x, imgHeight - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)