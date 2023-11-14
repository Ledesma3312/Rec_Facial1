import cv2
face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

#Ciclo se repite para tomar las fotos comofotogramas
while True:
    _, img= cap.read()
    #convertimos a color gris las imagenes
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #declaramos la variable Faces para la deteccion de rostros 
    #los parametros de la funcion es para ir detectando los rotros
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #este ciclo espara trakear la cara con rectangulos
    for(x, y, w, h) in faces:
        #los valores del color y grosor de las linea delrectangulo
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0),2)
    #muestra los que stan hacuendo el programa en una ventanas
    cv2.imshow('imag',img)
    #asignamos al valor de k el valor de 27 que en codigo assci es esc para cerrar el programa.
    k= cv2.waitKey(30) #el 30 es para el valor en milisegundos para revisar si se esta precionanado unatecla 
    if k == 27:
        break
cap.release()
         




