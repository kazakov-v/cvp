from time import time
import cv2

t = time()
s = 0.0
n = 0
# Открываем камеру с индексом 0 (первая доступная камера)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560//1)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440//1)

if not cap.isOpened():
    print("Ошибка! Камера не доступна.")
else:
    while True:
        # Читаем кадр из камеры
        ret, frame = cap.read()

        if not ret:
            break

        # Отображаем окно с изображением
        cv2.imshow('Web Camera', frame)

        dt = time() - t
        s += dt
        n += 1
        print(s / n)
        t = time()
        # print(frame.shape)

        # Остановка цикла по нажатию клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
