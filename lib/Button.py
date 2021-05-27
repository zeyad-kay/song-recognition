import tkinter as tk

class Button(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master,**kwargs)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_click(self,callback):
        """Execute function when the button is clicked.

        Args:
            callback (function): Function to be executed when the button is clicked.
        """        
        self["command"] = callback
    
    def on_enter(self, e):
        self["background"] = self["activebackground"]

    def on_leave(self, e):
        self["background"] = self.defaultBackground