# importing cv2 
import cv2 
   
# path 
path = 'fundamento_python/openCV/proyecto_facial/people.png'
# Reading an image in default mode
src = cv2.imread(path)
   
# Window name in which image is displayed
window_name = 'Image'
  
# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2GRAY color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )
  
# Displaying the image 
cv2.imshow(window_name, image)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

detected_faces = face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=4)