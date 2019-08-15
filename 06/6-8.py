import cv2

def on_mouse(event,x,y,flags,param):
    rect_start = (0,50)
    rect_end = (50,0)

    if event == cv2.EVENT_LBUTTONDOWN:
        rect_start = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        rect_end = (x,y)

    cv2.rectangle(img,rect_start,rect_end,(50,255,255),2)

img = cv2.imread("lena.jpg")
cv2.namedWindow('test')
cv2.setMouseCallback("test",on_mouse)


while(1):
    cv2.imshow("test",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
