import cv2
from cv2 import waitKey

img = cv2.imread("rawrrr.jpg")

print(type(img))
print(img.size)
print(img.dtype)
print(img.shape) 

#ekstrasi layer
b, g, r = cv2.split(img)
b = img[...,0]
g = img[...,1]
r = img[...,2]

hsv = cv2.cvtColor(img, cv2. COLOR_BGR2HSV);

# Menampilkan Gambar
cv2.imshow('patung',img)
cv2.imshow('Biru' ,b)
cv2.imshow('Hijau' ,g)
cv2.imshow('Merah' ,r)
cv2.imshow("Citra HSV", hsv)
waitKey(0)
# hsv = cv2.cvtColor(img, cv2. COLOR_BGR2HSV);
