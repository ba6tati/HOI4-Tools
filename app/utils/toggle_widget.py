from customtkinter import *
from tkinter import *

def toggle_widget(widget):
    """Toggles CTk/Tkinter widgets
    
    Keyword arguments:
    widget -- The widget to toggle
    Return: None
    """
    
    print(widget._state)
    if widget._state == 'normal':
        print('Toggle off')
        widget.configure(state='disabled')
    elif widget._state == 'disabled':
        print('Toggle on')
        widget.configure(state='normal')