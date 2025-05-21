from time import time
import cv2
from PIL import ImageTk, Image
import tkinter as tk

t = time()
s = 0.0
n = 0


# Функция обновления кадра с вебкамеры
def update_frame():
    # Захват нового кадра с вебкамеры
    ret, frame = cap.read()
    global t, s, n
    dt = time() - t
    s += dt
    n += 1
    print(s / n)
    t = time()

    if ret:
        # Преобразование формата кадров OpenCV в формат, понятный Tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Масштабирование изображения (при необходимости)
        # img = cv2.resize(img, (width, height))

        # Создание изображения Tkinter
        photo = Image.fromarray(img)
        photo = ImageTk.PhotoImage(image=photo)

        # Обновление Label с новым изображением
        label.config(image=photo)
        label.image = photo

    # Повторение функции каждые ~33 мс (~30 FPS)
    root.after(1, update_frame)


#  Настройка главного окна Tkinter
root = tk.Tk()
root.title("Webcam Viewer")

# Размеры окна
width, height = 2560//2, 1440//2

# Открытие видеопотока от первой доступной веб-камеры (номер устройства 0)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560//1)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440//1)
if not cap.isOpened():
    print("Ошибка открытия веб-камеры.")
    exit()

# Метка для отображения изображений
label = tk.Label(root)
label.pack()

# Запуск цикла обновления кадров
update_frame()

# Главный цикл приложения
root.mainloop()
