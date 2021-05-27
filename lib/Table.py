from tkinter import ttk
from tkinter.constants import NO

class Table(ttk.Treeview):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        for col in kwargs["columns"]:
            self.column(col,width=200,anchor="center")
            self.heading(col, text=col)

    def bulk_insert(self,rows=[()]):
        """Inserts multiple items in a single call

        Args:
            rows (list, optional): List of tuples containing the data. Defaults to [()].
        """        
        for index,row in enumerate(rows):
            self.insert(parent="",index=index,text=f"{index}",values=row)

    def clear(self):
        """Delete all items in the table
        """        
        for row in self.get_children():
            self.delete(row)