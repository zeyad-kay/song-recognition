from Mixer import Mixer
from lib import Button, Table
from File_Explorer import File_Explorer
from core import MP3, Hash, Comparator
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.create_widgets()
        self.bind("<<Detection>>",lambda e:self.detect_song())
    
    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid(sticky="nswe")
        self.create_mixer_panel()
        self.create_detection_panel()
        self.create_songs_table()
   
    def create_mixer_panel(self):
        container = tk.LabelFrame(self,relief="groove",text="Mixer")
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        
        mixer = Mixer(container)
        container.grid(row=0,column=1,sticky="nswe",padx=10,pady=20)
        mixer.grid(row=0,column=0,sticky="nswe",padx=10,pady=20)

    def create_detection_panel(self):
        container = tk.LabelFrame(self,relief="groove",text="Detect Song")
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        detect_btn = Button(container,activebackground="sky blue",relief="groove",text="Detect Song")
        detect_btn.on_click(self.upload_song)
        detect_btn.grid(row=0,column=0,padx=20,ipadx=40,pady=20)
        container.grid(row=0,column=0,sticky="nswe",padx=10,pady=20)

    def upload_song(self):
        filename = File_Explorer.open()
        if filename is None:
            return

        self.song, self.Fs = MP3.read(filename,60) # read only 60 seconds
        self.mixed_song = self.song
        self.event_generate("<<Detection>>")
    
    def detect_song(self):
        print("Generating features...")
        # spectrogram
        spectrum = MP3.get_spectrogram(self.mixed_song)
        features = MP3.get_features(self.mixed_song,spectrum,self.Fs)
        
        print("Generating Hashes...")
        # hashes
        hashes = {
            "spectrogram_hash": Hash.generate_hash_code(spectrum),
            "feature_1": Hash.generate_hash_code(features[0]),
            "feature_2": Hash.generate_hash_code(features[1])
        }
        
        print("Comparing Hashes...")
        # Compare hashes
        songs = Comparator.get_similar_songs(hashes)        
        # update songs table
        print("Finished.")
        self.update_songs_table(songs)

    def create_songs_table(self):
        
        container = tk.LabelFrame(self,relief="groove",text="Index Table")
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        columns = ("Song Name" ,"Similarity Index")
        self.table = Table(container,columns=columns)
        
        container.grid(row=1,column=0,columnspan=2,sticky="nswe",padx=10,pady=20)
        self.table.grid(row=0,column=0,columnspan=2,sticky="nswe",padx=10,pady=20)

    def update_songs_table(self,songs=[()]):
        """Update table with new songs their similarity index.

        Args:
            songs (list, optional): List of tuples of songs. 
            Each tuple contains the song name and similarity index . Defaults to [()].
        """                
        self.table.clear()
        self.table.bulk_insert(songs)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("app")
    root.minsize(600,500)
    app = Application(master=root)
    app.mainloop()
