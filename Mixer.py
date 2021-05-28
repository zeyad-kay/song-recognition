from core import MP3
import tkinter as tk
from lib import Slider, Button
from File_Explorer import File_Explorer

class Mixer(tk.Frame):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.song2 = None
        self.mixed_song = None

        self.mix_btn = Button(self,activebackground="sky blue",relief="groove",text="Mix")
        self.mix_btn.on_click(self.open_file)
        self.mix_btn.grid(row=0,column=0,padx=20,ipadx=40,pady=5)
        
        self.mix_slider = Slider(self, from_=0,orient="horizontal", resolution=1, to=100)
        self.mix_slider.on_change(self.mix,lazy=True)
        self.mix_slider.grid(row=1,column=0,padx=20,ipadx=40,pady=5)

    def mix(self,value):
        if self.song2 is None:
            return
        self.master.master.mixed_song = self.song2 * value/100 + self.master.master.song * (1 - value/100)      
        self.master.master.event_generate("<<Detection>>")

    def open_file(self):
        filename = File_Explorer.open()
        
        if filename:
            self.song2, self.Fs = MP3.read(filename,60) # read only 60 seconds
