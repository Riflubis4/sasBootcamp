#import library opencv

import cv2

def main(capture):
    while True:
        #print(capture.read())
        #baca kamera
        ret, frame = capture.read() 

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    frame.release()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    camera = cv2.VideoCapture(0)
    main(camera)



