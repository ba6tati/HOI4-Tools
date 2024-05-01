from customtkinter import *
from tkinter import filedialog

class MainWindow(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.mod_path = str()
        
        self.mod_descriptor_lbl = CTkLabel(self.master, text='Mod Descriptor: ')
        self.mod_descriptor = CTkEntry(self.master, placeholder_text='Mod Descriptor')
    
        self.select = CTkButton(self.master, text='Select', command=self.select_mod_descriptor)
        
        self.create_country_btn = CTkButton(self.master, text='Create Country', command=self.create_country)
        
        self.mod_descriptor_lbl.grid(column=0, row=0)
        self.mod_descriptor.grid(column=1, row=0)
        self.select.grid(column=2, row=0)
        
        self.create_country_btn.grid(column=0, row=1, columnspan=3)
        
        self.mod_descriptor.bind('<Key>', self.get_mod_path)
        
        try:
            with open('cache/mod_descriptor.txt', 'r') as f:
                mod_descriptor = f.readlines()[0]
                self.mod_descriptor.insert(0, mod_descriptor)
        except (FileNotFoundError, IndexError):
            pass
        
        if self.mod_descriptor.get():
            self.get_mod_path()
    
    def select_mod_descriptor(self):
        mod_descriptor = filedialog.askopenfilename(title='Select Mod Descriptor', filetypes=(('Descriptor', '*.mod'), ('All types', '*.*')))
        
        self.mod_descriptor.delete(0, END)
        self.mod_descriptor.insert(0, mod_descriptor)
        
        with open('cache/mod_descriptor.txt', 'w+') as f:
            f.write(mod_descriptor)
        
    def create_country(self):
        window = CTkToplevel(self.master)
        CreateCountryWindow(window, self.mod_path)
        window.mainloop()
        
    def get_mod_path(self, event=None):
        try:
            descriptor = self.mod_descriptor.get()
            with open(descriptor, 'r') as f:
                for line in f.readlines():
                    if line.strip().startswith('path'):
                        self.mod_path = line.split('=')[1].strip().replace('"', '')
                        # print(self.mod_path)
        except FileNotFoundError:
            pass