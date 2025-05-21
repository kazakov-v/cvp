import cv2
import numpy as np
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QWidget


class CameraWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.cap = cv2.VideoCapture(0)  # Используем первую камеру (обычно встроенная)
        if not self.cap.isOpened():
            raise ValueError("Камера не доступна.")
        self.timer.start(30)  # Обновляем кадр каждые ~30 мс (~33 FPS)

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Web Камера')
        self.label = QLabel(self)
        # self.layout().addWidget(self.label)

    def update_frame(self):
        ret, frame = self.cap.read()  # Получаем новый кадр
        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qimg = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            self.label.setPixmap(pixmap.scaled(self.label.size(), aspectRatioMode=1))  # Масштабируем картинку под размер окна

    def closeEvent(self, event):
        self.timer.stop()
        self.cap.release()
        event.accept()


def main():
    app = QApplication([])
    ex = CameraWindow()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()
