# face_eye_detection_haarcascade
A simple program to detect your face, eye, and smile in real time
### To test the program on your device
1. Make sure your webcam is connected to your device.
2. Run the ```faceDetector.py``` on the separate window of the shell
<br />



Used [CascadeClassifier](https://docs.opencv.org/2.4/doc/tutorials/objdetect/cascade_classifier/cascade_classifier.html) 
to detect objects in a video stream through camera or an image. With further development, this can be used with mobile devices or other web frameworks 
<br />
<br />
API called [detectMultiScale](https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html?highlight=detectmultiscale#cascadeclassifier-detectmultiscale) 
from CascadeClassifier gives you coordinate information of detected objects of different sizes in the input image.
Trained dataset of faces is from [OpenCV GitHub](https://github.com/opencv/opencv) repository.
<br />
<br />
Check out https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html for more detailed information.


![alt text](https://github.com/sungw5/face_eye_detection_haarcascade/blob/master/testpic/testpic2.png?raw=true)
![alt text](https://github.com/sungw5/face_eye_detection_haarcascade/blob/master/testpic/testpic1.png?raw=true)
