#import library opencv

import cv2

def main(capture):
    face_dataset = '/home/ariflubis/Documents/assets/haarcascade_frontalface_default.xml'
    eye_dataset = '/home/ariflubis/Documents/assets/haarcascade_eye.xml'
    smile_dataset = '/home/ariflubis/Documents/assets/smile_cascade.xml'
    upperbody_dataset = '/home/ariflubis/Documents/assets/haarcascade_upperbody.xml'

    face_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)
    smile_cascade = cv2.CascadeClassifier(smile_dataset)
    upperbody_cascade = cv2.CascadeClassifier(upperbody_cascade)


    while True:
        ret, frame = capture.read() 

        #ubah warna ke dari BGR ke grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        #Deteksi haarcascde
        faces = face_cascade.detectMultiScale(gray, scaleFactor=2)

        #untuk setiap wajah yang terdeteksi
        for (x, y, w, h) in faces:
            #simpan koordinat titik tengah wajah
            center = (x + w //2, y + h//2)
            #Tampilan lingkaran
            cv2.rectangle(frame, center, (w + x, h + y), (0, 255, 0), 2)

            #tentukan wilayah wajah yang terdeteksi
            face_roi = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(face_roi)

            #untuk setiap mata terdeteksi
            for (x2, y2, w2, h2) in eyes:
                #simpan koordinat titik tengah dari mata yg terdeteksi
                eye_center = (x + x2 + w2//2, y + y2 + h2//2)
                #simpan nilai jari2 dari mata yang terdeteksi
                radius = int(round((w2 + h2) * 0.25))
                #Tampilkan lingkaran
                frame = cv2.circles(frame, eye_center, radius, 0, 0, 360, (0, 255, 0), 2)

            
            smile = smile_cascade.detectMultiScale(face_roi)

            for (x3, y3, w3, h3) in upperbodies:
                frame = cv2.rectangle 

            if len(smiles) > 0:
                for (x4,y4, w4, h4) in smiles:
                    smile_center = (x + x4 + w4//2, y + y4 + h4//2)
                    radius = int(round((w4+h4) * 0.25))
                    cv2.rectangle(frame, smile_center, radius (0, 255, 0), 2)
                    cv2.putText(frame, 'smile', (x4,y4), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            else:
                cv2.rectangle(frame, smile_center, radius , (0, 0, 255), 2)
                cv2.putText(frame, 'not smile', (x4,y4), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)


        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    frame.release()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    camera = cv2.VideoCapture(0)
    main(camera)



