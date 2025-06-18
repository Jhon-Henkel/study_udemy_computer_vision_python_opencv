import cv2

image = cv2.imread('image.jpg')
image = cv2.resize(image, (600, 500))
greyImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cannyImage = cv2.Canny(greyImage, 30, 200)
closeImage = cv2.morphologyEx(cannyImage, cv2.MORPH_CLOSE, (7, 7))

contours, hierarchy = cv2.findContours(closeImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
objNumber = 1

for contour in contours:
    # cv2.drawContours(image, [contour], -1, (255, 0, 0), 2)
    x, y, w, h = cv2.boundingRect(contour)
    cv2.imwrite(f'objects/object_{objNumber}.jpg', image[y:y + h, x:x + w])
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    objNumber += 1

cv2.imshow('image', image)
cv2.imshow('greyImage', greyImage)
cv2.imshow('cannyImage', cannyImage)
cv2.imshow('closeImage', closeImage)
cv2.waitKey(0)
