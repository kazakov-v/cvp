import tkinter as tk
import cv2
from PIL import Image, ImageTk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=1)
        self.streaming_image = self.canvas.create_image(
            0, 0, anchor="nw", image=None
        )

    def show_frame(self):
        _, frame = self.vid_cap.read()
        print(frame.shape)
        # frame = cv2.resize(frame, (696, 486))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        self.latest_img = ImageTk.PhotoImage(image=img)
        self.canvas.itemconfig(self.streaming_image, image=self.latest_img)
        self.after(1, self.show_frame)

    def start_video(self, path=None):
        self.vid_cap = cv2.VideoCapture(path)
        self.vid_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560//2)
        self.vid_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440//2)

        self.show_frame()


root = GUI()
root.start_video(0)
root.mainloop()
