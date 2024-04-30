from customtkinter import CTkFrame, CTkLabel

class MainWindow(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = CTkLabel(self, text='Hello, world!')
        self.label.pack()