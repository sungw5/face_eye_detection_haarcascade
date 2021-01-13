import cv2

# load the trained data on frontal faces from opencv
trainedFaceData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('imagepath')
#videoCapture = cv2.VideoCapture('videopath)
videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()

    # convert to grayscale (!IMPORTANT)
    grayscaledImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # gives coordinates (x,y,w,h) in 2d array
    faceCoordinates = trainedFaceData.detectMultiScale(grayscaledImg)

    
    for i in range(len(faceCoordinates)):
        (x, y, w, h) = faceCoordinates[i]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # imgfile, coordinates1, coordinates2, color, thickness
        print("x: ", x, "y: ", y, "width from offset: ", w, "height from offset: ", h)

    cv2.imshow('Video', frame) #display

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
videoCapture.release()
cv2.destroyAllWindows()
print("************  Exit Camera  ************ ")