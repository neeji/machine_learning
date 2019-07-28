import cv2
video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    cv2.imshow("video_tab_1", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
video.release()
cv2.destroyAllWindows()
