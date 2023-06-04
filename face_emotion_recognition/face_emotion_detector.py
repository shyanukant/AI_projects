from facial_emotion_recognition import EmotionRecognition
import cv2

''' Make this change
 MY_LOCATION = 'cpu' 
 in load funtion 
 in yourenv\Lib\site-packages\torch\serialization.py 
 '''
er = EmotionRecognition(device='cpu')
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame = er.recognise_emotion(frame, return_type='BGR')
    cv2.imshow('Check Emotions', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()