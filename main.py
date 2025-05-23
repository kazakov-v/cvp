import cv2
import numpy as np
from cvp import gui


def mouse_callback(event, x, y, flags, param):
    # if flags & cv2.EVENT_FLAG_LBUTTON:
    #     print('++++++++++++++++')

    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Left button clicked at ({x}, {y})')
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f'Right button clicked at ({x}, {y})')
    elif event == cv2.EVENT_MOUSEMOVE:
        print(f'Mouse moved to ({x}, {y})')


window_name = 'CVP'
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, mouse_callback)

p = gui.Point(1)
a = np.zeros([1080//2, 1920//2, 3])
while True:
    cv2.imshow(window_name, a)
    key = cv2.waitKey(1)
    if key != -1:
        print(key)
    if key & 0xFF == ord('q'):
        break
