import cv2

img = cv2.imread("rawrrr.jpg")

#konversi BGR ke ruang warna HSV
hsv = cv2.cvtColor(img, cv2. COLOR_BGR2HSV);
cv2.imshow("Citra HSV", hsv)
cv2.waitKey(0)