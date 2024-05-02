import cv2

img1 = cv2.imread("kotak.jpg")
print(img1.shape)
print(img1.dtype)

img2 = cv2.imread("bundar.jpg")
print(img2.shape)
print(img2.dtype)

width = 300
height = 300
dim = (width,height)

img1 = cv2.resize(img1,dim, Interpolation=cv2.INTER_AREA)
img2 = cv2.resize(img2,dim, Interpolation=cv2.INTER_AREA)

imggray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imggray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

bw1 = cv2.threshold(imggray1, 125, 255, cv2.THRESH_BINARY)
bw2 = cv2.threshold(imggray2, 125, 255, cv2.THRESH_BINARY)

op_and = cv2.bitwise_and(img1, img2)
op_or = cv2.bitwise_or(img1, img2)

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Hasil And", op_and)
cv2.imshow("Hasil Or", op_and)
cv2.waitKey(0)