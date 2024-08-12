import cv2
screen = cv2.VideoCapture("bb3.mp4")

#loadTracker
tracker = cv2.TrackerCSRT_create()

#capture the first frame
ret, frame = screen.read()

#select the bounding box
bbox = cv2.selectROI("tracking", frame, False)

#initialize tracker
ok = tracker.init(frame, bbox)
print(bbox)

#draw boundBox
def drawbox(frame,bbox):
    #get the value of bbox
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

    #draw the rectangle using cv2
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3,1)

    #Write a text or a frame
    cv2.putText(frame,"Tracking",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
while True:
    #read a new frame
    ret, frame = screen.read()

    #update tracker
    ok, bbox = tracker.update(frame)

    if ok:
        #draw the bounding box
        drawbox(frame, bbox)

    else:
        #if the tracker is not found, print a message
        cv2.putText(frame,"Tracking failed",(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0),2)

    #display the frame
    cv2.imshow("tracking", frame)
    key = cv2.waitKey(1)
    if key == 32:
        break

    screen.release()
    cv2.destroyAllWindows()
    





