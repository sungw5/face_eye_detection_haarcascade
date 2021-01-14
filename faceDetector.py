import cv2

# load the trained data on frontal faces from opencv
trainedFaceData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
trainedEyeData = cv2.CascadeClassifier('haarcascade_eye.xml')
trainedSmileData = cv2.CascadeClassifier('haarcascade_smile.xml')

#img = cv2.imread('imagepath')
#videoCapture = cv2.VideoCapture('videopath)
videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()

    # convert to grayscale (!IMPORTANT)
    grayscaledImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # gives coordinates (x,y,w,h) in 2d array
    faceCoordinates = trainedFaceData.detectMultiScale(grayscaledImg) # face
    eyeCoordinates = trainedEyeData.detectMultiScale(grayscaledImg) # Eye
    smailCoordinates = trainedEyeData.detectMultiScale(grayscaledImg) # Eye

    # face
    for i in range(len(faceCoordinates)):
        (x, y, w, h) = faceCoordinates[i]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3) # imgfile, coordinates1, coordinates2, color, thickness
        print("x: ", x, "y: ", y, "width from offset: ", w, "height from offset: ", h)

    # Eye
    for j in range(len(eyeCoordinates)):
        (x, y, w, h) = eyeCoordinates[j]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (3, 94, 252), 2) # imgfile, coordinates1, coordinates2, color, thickness

    # Smile
    for k in range(len(smailCoordinates)):
        (x, y, w, h) = smailCoordinates[k]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 1) # imgfile, coordinates1, coordinates2, color, thickness

    cv2.imshow('Video', frame) #display

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
videoCapture.release()
cv2.destroyAllWindows()
print("************  Exit Camera  ************ ")