import cv2

def main(capture):
    upperbody_dataset = '/home/ariflubis/Documents/assets/haarcascade_upperbody.xml'
    face_dataset = '/home/ariflubis/Documents/assets/haarcascade_frontalface_default.xml'
    eye_dataset = '/home/ariflubis/Documents/assets/haarcascade_eye.xml'
    smile_dataset = '/home/ariflubis/Documents/assets/smile_cascade.xml'

    upperbody_cascade = cv2.CascadeClassifier(upperbody_dataset)
    face_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)
    smile_cascade = cv2.CascadeClassifier(smile_dataset)

    while True:
        ret, frame = capture.read()

        # convert color from BGR to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # detect upper body
        upperbodies = upperbody_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # for each upper body detected
        for (x, y, w, h) in upperbodies:
            # draw green rectangle around the upper body
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # detect face within the upper body region
            faces = face_cascade.detectMultiScale(gray[y:y+h, x:x+w], scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # for each face detected
            for (fx, fy, fw, fh) in faces:
                # draw green rectangle around the face
                cv2.rectangle(frame, (x + fx, y + fy), (x + fx + fw, y + fy + fh), (0, 255, 0), 2)

                # determine the region of interest for the face
                face_roi = gray[y + fy:y + fy + fh, x + fx:x + fx + fw]

                # detect eyes within the face region
                eyes = eye_cascade.detectMultiScale(face_roi)

                # for each eye detected
                for (ex, ey, ew, eh) in eyes:
                    # draw green rectangle around the eye
                    cv2.rectangle(frame, (x + fx + ex, y + fy + ey), (x + fx + ex + ew, y + fy + ey + eh), (0, 255, 0), 2)

                # detect smile within the face region
                smiles = smile_cascade.detectMultiScale(face_roi)

                # if smile is detected
                if len(smiles) > 0:
                    # draw green rectangle around the smile
                    for (sx, sy, sw, sh) in smiles:
                        cv2.rectangle(frame, (x + fx + sx, y + fy + sy), (x + fx + sx + sw, y + fy + sy + sh), (0, 255, 0), 2)

                    # display green text on the face
                    cv2.putText(frame, 'Smiling', (x + fx, y + fy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                else:
                    # if no smile is detected, draw red rectangle around the face
                    cv2.rectangle(frame, (x + fx, y + fy), (x + fx + fw, y + fy + fh), (0, 0, 255), 2)

                    # display red text on the face
                    cv2.putText(frame, 'Not Smiling', (x + fx, y + fy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # display the frame
        cv2.imshow('Frame', frame)

        # break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # release the camera and close all windows
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)
