import cv2
import numpy as np

def get_shape(approx):
    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            return "Square"
        else:
            return "Rectangle"
    elif len(approx) == 8:
        return "Octagon"
    elif len(approx) > 10:
        return "Circle"
    else:
        return "Undefined"

def get_color_name(hue):
    if 0 <= hue <= 20 or 160 <= hue <= 180:
        return "Red"
    elif 20 < hue < 40:
        return "Orange"
    elif 40 <= hue < 80:
        return "Yellow"
    elif 80 <= hue < 140:
        return "Green"
    elif 140 <= hue < 160:
        return "Blue"
    else:
        return "Undefined"

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
    init_trackbars('COLOR')

    while True:
        ret, frame = capture.read()

        # Color detection
        lower_hsv, upper_hsv = get_hsv_values('COLOR')
        thresh = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower_hsv, upper_hsv)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_result = frame.copy()

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            epsilon = 0.04 * cv2.arcLength(largest_contour, True)
            approx = cv2.approxPolyDP(largest_contour, epsilon, True)
            shape = get_shape(approx)
            color_hue = cv2.mean(frame, mask=thresh)[0]
            color_name = get_color_name(color_hue)

            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.putText(frame_result, f'{color_name} {shape}', (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.drawContours(frame_result, [approx], 0, (255, 255, 255), 2)

        cv2.imshow('Object Detection', frame_result)
        cv2.imshow('Frame', frame)
        cv2.imshow('thresh', thresh)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)
