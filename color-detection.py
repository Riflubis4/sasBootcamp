import cv2

def callback(_):
    pass

def init_trackbars(color_name):
    cv2.namedWindow(f'{color_name} Trackbars')
    cv2.createTrackbar(f'LH_{color_name}', f'{color_name} Trackbars', 0, 255, callback)
    cv2.createTrackbar(f'LS_{color_name}', f'{color_name} Trackbars', 0, 255, callback)
    cv2.createTrackbar(f'LV_{color_name}', f'{color_name} Trackbars', 0, 255, callback)
    cv2.createTrackbar(f'UH_{color_name}', f'{color_name} Trackbars', 255, 255, callback)
    cv2.createTrackbar(f'US_{color_name}', f'{color_name} Trackbars', 255, 255, callback)
    cv2.createTrackbar(f'UV_{color_name}', f'{color_name} Trackbars', 255, 255, callback)

def get_hsv_values(color_name):
    lower_hue = cv2.getTrackbarPos(f'LH_{color_name}', f'{color_name} Trackbars')
    lower_sat = cv2.getTrackbarPos(f'LS_{color_name}', f'{color_name} Trackbars')
    lower_val = cv2.getTrackbarPos(f'LV_{color_name}', f'{color_name} Trackbars')
    upper_hue = cv2.getTrackbarPos(f'UH_{color_name}', f'{color_name} Trackbars')
    upper_sat = cv2.getTrackbarPos(f'US_{color_name}', f'{color_name} Trackbars')
    upper_val = cv2.getTrackbarPos(f'UV_{color_name}', f'{color_name} Trackbars')
    return (lower_hue, lower_sat, lower_val), (upper_hue, upper_sat, upper_val)

def main(capture):
    init_trackbars('YELLOW')
    init_trackbars('BROWN')
    init_trackbars('WHITE')

    while True:
        ret, frame = capture.read()

        # Yellow color detection
        lower_hsv_y, upper_hsv_y = get_hsv_values('YELLOW')
        thresh_y = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower_hsv_y, upper_hsv_y)
        contours_y, _ = cv2.findContours(thresh_y, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_y = frame.copy()

        if contours_y:
            largest_contour_y = max(contours_y, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour_y)
            cv2.putText(frame_y, 'YELLOW', (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
            cv2.rectangle(frame_y, (x, y), (w + x, h + y), (0, 255, 255), 2)

        # Brown color detection
        lower_hsv_br, upper_hsv_br = get_hsv_values('BROWN')
        thresh_br = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower_hsv_br, upper_hsv_br)
        contours_br, _ = cv2.findContours(thresh_br, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_br = frame.copy()

        if contours_br:
            largest_contour_br = max(contours_br, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour_br)
            cv2.putText(frame_br, 'BROWN', (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (42, 42, 165), 2)
            cv2.rectangle(frame_br, (x, y), (w + x, h + y), (42, 42, 165), 2)

        # White color detection
        lower_hsv_w, upper_hsv_w = get_hsv_values('WHITE')
        thresh_w = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower_hsv_w, upper_hsv_w)
        contours_w, _ = cv2.findContours(thresh_w, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_w = frame.copy()

        if contours_w:
            largest_contour_w = max(contours_w, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour_w)
            cv2.putText(frame_w, 'WHITE', (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
            cv2.rectangle(frame_w, (x, y), (w + x, h + y), (255, 255, 255), 2)

        
        cv2.imshow('Yellow Detection', frame_y)
        cv2.imshow('Brown Detection', frame_br)
        cv2.imshow('White Detection', frame_w)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)
