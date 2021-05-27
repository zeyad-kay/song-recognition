import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=2)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

        self.grid(sticky="nswe")
        self.mixPanel()
        self.openSong()
        self.indexTable()
   
    def mixPanel(self):
        self.mixFrame = tk.LabelFrame(self.master,relief="groove",text="Mixing panel")
        self.mixFrame.grid_columnconfigure(0, weight=1)
        self.mixFrame.grid_rowconfigure(0, weight=1)
        self.mixFrame.grid_rowconfigure(1, weight=1)
        self.mix = HoverButton(self.mixFrame,activebackground="sky blue",relief="groove",text="Mix")
        self.mix.grid(row=0,column=0,padx=20,ipadx=40,pady=5)
        self.mixSlider = tk.Scale(self.mixFrame, from_=0,orient="horizontal", resolution=1, to=100)
        self.mixSlider.grid(row=1,column=0,padx=20,ipadx=40,pady=5)
        self.mixFrame.grid(row=0,column=1,sticky="nswe",padx=10,pady=20)
        

 
    def openSong(self):
        self.exploreFrame = tk.LabelFrame(self.master,relief="groove",text="open song")
        self.exploreFrame.grid_columnconfigure(0, weight=1)
        self.exploreFrame.grid_rowconfigure(0, weight=1)

        self.explore = HoverButton(self.exploreFrame,activebackground="sky blue",relief="groove",text="open song")
        self.explore.grid(row=0,column=0,padx=20,ipadx=40,pady=20)
        self.exploreFrame.grid(row=0,column=0,sticky="nswe",padx=10,pady=20)

    def indexTable(self):
        self.test={
            "hala":"40%",
            "ddd":"420%",
            "fawf":"440%",
            "ffq":"42%",
            "halwwawa":"45%",
        }

        self.tableFrame = tk.LabelFrame(self.master,relief="groove",text="Index Table")
        self.tableFrame.grid_columnconfigure(0, weight=1)
        self.tableFrame.grid_rowconfigure(0, weight=1)
        self.indexTree = ttk.Treeview(self.tableFrame)
        self.indexTree["columns"] = ("Song Name" ,"Similarity Index")
        self.indexTree.column("#0",width=20,anchor="center")
        self.indexTree.column("Song Name",width=200,anchor="center")
        self.indexTree.column("Similarity Index",width=200,anchor="center")
        
        self.indexTree.heading("#0", text="")
        self.indexTree.heading("Song Name", text="Song Name")
        self.indexTree.heading("Similarity Index", text="Similarity Index")
        self.treeInsert(self.test)
        self.indexTree.grid(row=0,column=0,padx=20,ipadx=40,pady=20)
        self.tableFrame.grid(row=1,column=0,columnspan=2,sticky="nswe",padx=10,pady=20)

    def treeInsert(self,result):
        for index,song in enumerate(result):
            self.indexTree.insert(parent="",index=index+1,text=f"{index+1}st",values=(song,result[song]))

    def edit(self,result):
        x = self.indexTree.get_children()
        for item in x: 
            self.indexTree.delete(item)
        self.treeInsert(result)

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

if __name__ == "__main__":
    root = tk.Tk()
    root.title("app")
    root.minsize(600,500)
    app = Application(master=root)
    app.mainloop()
