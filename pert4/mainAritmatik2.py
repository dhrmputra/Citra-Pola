from turtle import width
import cv2

img1 = cv2.imread("gambar.jpg")
img2 = cv2.imread("gambar2.jpg")

width = 256
height = 256
dim = (width, height)

img1 = cv2.resize(img1, dim, interpolation= cv2.INTER_AREA)
img2 = cv2.resize(img2, dim, interpolation= cv2.INTER_AREA)

img3 = img1 + img2

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Hasil", img3)
cv2.imshow("Image 1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()