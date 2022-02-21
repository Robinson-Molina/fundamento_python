import cv2
import os
import imutils
personName = 'Gaby'
dataPath = 'C:/Users/Gaby/Desktop/Reconocimiento Facial/Data'#Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName
if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video.mp4')
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0
