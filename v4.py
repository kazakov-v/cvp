from time import time
import cv2
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

t = time()
s = 0.0
n = 0


class CameraViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.video_label = QLabel(self)

        # Настройка таймера для регулярного обновления кадра
        timer = QTimer(self)
        timer.timeout.connect(self.update_frame)
        timer.start(1)  # обновлять каждые ~30 мс (~33 FPS)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        self.setLayout(layout)
        self.setWindowTitle("Камера")
        self.resize(int(2560/2), int(1440/2))

    def update_frame(self):
        ret, frame = cap.read()
        if not ret:
            return

        global t, s, n
        dt = time() - t
        s += dt
        n += 1
        print(s / n)
        t = time()

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.video_label.width(), self.video_label.height(), aspectRatioMode=True)
        self.video_label.setPixmap(QPixmap.fromImage(p))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cap = cv2.VideoCapture(0)  # 0 означает первую камеру устройства
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560//2)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440//2)

    viewer = CameraViewer()
    viewer.show()
    sys.exit(app.exec_())
