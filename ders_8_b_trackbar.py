import cv2

def nothing():
    pass
cv2.namedWindow('enespolat')
cv2.createTrackbar('xVal','enespolat',25,640,nothing)
cv2.createTrackbar('yVal','enespolat',25,480,nothing)

cv2.createTrackbar('en','enespolat',25,640,nothing)
cv2.createTrackbar('boy','enespolat',25,480,nothing)
cam=cv2.VideoCapture(0)

while(cam.isOpened()):
    _,frame=cam.read()
    
    xVal=cv2.getTrackbarPos('xVal','enespolat')
    yVal=cv2.getTrackbarPos('yVal','enespolat')
    en=cv2.getTrackbarPos('en','enespolat')
    boy=cv2.getTrackbarPos('boy','enespolat')
    #cv2.circle(frame,(xVal,yVal),8,(0,255,0),-1)
    cv2.rectangle(frame,(xVal,yVal),(xVal+en,yVal+boy),(0,255,0),4)
    cv2.imshow('enespolat',frame)
    cv2.moveWindow('enespolat',0,35)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()