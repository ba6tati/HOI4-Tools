import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customtkinter import CTk
from config import WINDOW_TITLE, WINDOW_SIZE

from app.windows.main_window import MainWindow

class MainApplication(CTk):
    def __init__(self):
        super().__init__()
        
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)
        
        self.main_window = MainWindow(self)
        
        self.main_window.pack()
        
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()