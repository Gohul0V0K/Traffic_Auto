import cv2 as cv

img = cv.imread('1.jpg')

car_cascade = cv.CascadeClassifier('car.xml')

if car_cascade.empty():
    print("hi")
print(car_cascade)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cars = car_cascade.detectMultiScale(gray, 1.1, 2)

print(cars)

for(x,y,w,h) in cars:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)


cv.imshow("Detected Face",img)
