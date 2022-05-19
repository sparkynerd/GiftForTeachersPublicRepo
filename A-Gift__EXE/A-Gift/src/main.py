import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
from mixer import play
import time


class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


# demo :
root = tk.Tk()
root.title("ur gift XD")
lbl = ImageLabel(root)
lbl.pack()
try:
    lbl.load('assets\\button.gif')
except:
    try:
        lbl.load("..\\..\\A-Gift\\assets\\button.gif")
    except:
        lbl.load("..\\..\\..\\A-Gift\\assets\\button.gif")
print("Turn your volume up!")
time.sleep(1)
print("Loading...")
time.sleep(1.7)
print("Making the file awesome-er")
time.sleep(1.5)
print("[AWESOMENESS WARNING]")
try:
    play("mixtape\\remix\\its-raining-tacos.mp3")
except:
    try:
        play("..\\..\\A-Gift\\mixtape\\remix\\its-raining-tacos.mp3")
    except:
        play("..\\..\\..\\A-Gift\\mixtape\\remix\\its-raining-tacos.mp3")
root.mainloop()
