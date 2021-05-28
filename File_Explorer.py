from tkinter import filedialog

class File_Explorer():
    @staticmethod
    def open():
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("MP3 files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*"))) or None
        return filename