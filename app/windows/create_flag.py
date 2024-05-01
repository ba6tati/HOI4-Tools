from customtkinter import *
from shutil import copyfile
from tkinter import messagebox
from config import WINDOW_TITLE, WINDOW_SIZE

ideologies = ('all', 'democratic', 'communism', 'fascism', 'neutrality') # TODO: get from the hoi4 game
sizes = ('all', 'default', 'medium', 'small')

class CreateFlag(CTkToplevel):
    def __init__(self, master, mod_path=None, tag=None):
        super().__init__(master)
        
        self.title(WINDOW_TITLE + ' | Create Flag')
        self.geometry(WINDOW_SIZE)
        
        self.frame = CTkFrame(self)
        
        self.mod_path = CTkEntry(self.frame, placeholder_text='Mod Path')
        self.select_path_btn = CTkButton(self.frame, text='Select', command=self.select_directory)
        
        self.tag = CTkEntry(self.frame, placeholder_text='TAG')
        self.cosmetic_tag = CTkEntry(self.frame, placeholder_text='Cosmetic TAG')
        
        self.ideology_lbl = CTkLabel(self.frame, text='Ideology: ')
        self.ideology = CTkComboBox(self.frame, values=ideologies)
        
        self.size_lbl = CTkLabel(self.frame, text='Size: ')
        self.size = CTkComboBox(self.frame, values=sizes)
        
        self.generate_btn = CTkButton(self.frame, text='Generate', command=self.generate)
        
        self.mod_path.grid(row=0, column=0)
        self.select_path_btn.grid(row=0, column=1)
        self.tag.grid(row=1, column=0, columnspan=2)
        self.cosmetic_tag.grid(row=2, column=0, columnspan=2)
        self.ideology_lbl.grid(row=3, column=0)
        self.ideology.grid(row=3, column=1)
        self.size_lbl.grid(row=4, column=0)
        self.size.grid(row=4, column=1)
        self.generate_btn.grid(row=5, column=0, columnspan=2)
        
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        if mod_path:
            self.mod_path.insert(0, mod_path)
        if tag:
            self.tag.insert(0, tag)
        
        for widget in self.frame.winfo_children():
            widget.grid_configure(padx=10, pady=10, sticky=NSEW)
        
    def generate(self):
        mod_path = self.mod_path.get()
        tag = self.tag.get()
        cosmetic_tag = self.cosmetic_tag.get()
        if cosmetic_tag:
            cosmetic_tag += '_'
        ideology = self.ideology.get()
        size = self.size.get()
        
        self.tag.delete(0, END)
        self.cosmetic_tag.delete(0, END)
        self.ideology.set(ideologies[0])
        self.size.set(sizes[0])
        
        match size:
            case 'all':
                copyfile(f'templates/flags/default.tga', f'{mod_path}/gfx/flags/{tag}_{cosmetic_tag}{ideology}.tga')
                copyfile(f'templates/flags/medium.tga', f'{mod_path}/gfx/flags/medium/{tag}_{cosmetic_tag}{ideology}.tga')
                copyfile(f'templates/flags/small.tga', f'{mod_path}/gfx/flags/small/{tag}_{cosmetic_tag}{ideology}.tga')
                
        messagebox.showinfo('Successs', 'You have successfully generated country flag/s')
        
    def select_directory(self):
        mod_path = filedialog.askdirectory()
        
        if mod_path:
            self.mod_path.delete(0, END)
            self.mod_path.insert(0, mod_path)