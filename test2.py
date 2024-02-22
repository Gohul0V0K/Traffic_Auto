import cv2 as cv

car_cascade=cv.CascadeClassifier('car.xml')
capture=cv.VideoCapture('v1.mp4')

isTrue=True
while isTrue:
    isTrue,frame=capture.read()

    
    if isTrue:
        cv.imshow('video',frame)
        grey=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow("grey",grey)

        

        car_rect=car_cascade.detectMultiScale(grey,1.1,5)
        print(len(car_rect))
        for(x,y,w,h) in car_rect:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv.imshow("Detected cars",frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break


cv.waitKey(0)
