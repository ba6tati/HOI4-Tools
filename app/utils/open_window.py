from customtkinter import CTk
from tkinter import Tk
from typing import Union

def open_window(master: Union[CTk, Tk], window, **kwargs):
    """Cheks if the window is open and  if it is not then it opens it
    
    Keyword arguments:
    master -- master/root window
    window -- window class to open
    Return: None
    """
    
    opened = False
    for w in master.winfo_children():
        if isinstance(w, window):
            opened = True
    if not opened:
        window = window(master, **kwargs)
        window.after(10, window.lift)