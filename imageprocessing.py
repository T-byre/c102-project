import cv2
def take_snapshot():
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        print(ret)
        cv2.imwrite("img1.jpg", frame)
        result = False
    videocaptureobject.release()
    cv2.destroyAllWindows()
take_snapshot()