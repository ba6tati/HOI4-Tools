from customtkinter import *
from shutil import copyfile
from tkinter import messagebox
from config import WINDOW_TITLE, WINDOW_SIZE
from utils import make_directory_if_not_exists

ideologies = ('all', 'democratic', 'communism', 'fascism', 'neutrality') # TODO: get from the hoi4 game
sizes = ('all', 'default', 'medium', 'small')

class CreateFlag(CTkToplevel):
    def __init__(self, master, mod_path, tag):
        super().__init__(master)
        
        self.mod_path = mod_path
        self.tag = tag
        
        self.title(WINDOW_TITLE + ' | Create Flag')
        self.geometry(WINDOW_SIZE)
        
        self.frame = CTkFrame(self)

        self.cosmetic_tag = CTkEntry(self.frame, placeholder_text='Cosmetic TAG')
        
        self.ideology_lbl = CTkLabel(self.frame, text='Ideology: ')
        self.ideology = CTkComboBox(self.frame, values=ideologies)
        
        self.size_lbl = CTkLabel(self.frame, text='Size: ')
        self.size = CTkComboBox(self.frame, values=sizes)
        
        self.generate_btn = CTkButton(self.frame, text='Generate', command=self.generate)
        
        self.cosmetic_tag.grid(row=2, column=0, columnspan=2)
        self.ideology_lbl.grid(row=3, column=0)
        self.ideology.grid(row=3, column=1)
        self.size_lbl.grid(row=4, column=0)
        self.size.grid(row=4, column=1)
        self.generate_btn.grid(row=5, column=0, columnspan=2)
        
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        for widget in self.frame.winfo_children():
            widget.grid_configure(padx=10, pady=10, sticky=NSEW)
        
    def generate(self):
        cosmetic_tag = self.cosmetic_tag.get()
        if cosmetic_tag:
            cosmetic_tag += '_'
        ideology = self.ideology.get()
        size = self.size.get()
        
        #self.tag.delete(0, END)
        self.cosmetic_tag.delete(0, END)
        self.ideology.set(ideologies[0])
        self.size.set(sizes[0])
        
        make_directory_if_not_exists(f'{self.mod_path}/gfx/flags/medium')
        make_directory_if_not_exists(f'{self.mod_path}/gfx/flags/small')
        
        match size:
            case 'all':
                copyfile(f'templates/flags/default.tga', f'{self.mod_path}/gfx/flags/{self.tag}_{cosmetic_tag}{ideology}.tga')
                copyfile(f'templates/flags/medium.tga', f'{self.mod_path}/gfx/flags/medium/{self.tag}_{cosmetic_tag}{ideology}.tga')
                copyfile(f'templates/flags/small.tga', f'{self.mod_path}/gfx/flags/small/{self.tag}_{cosmetic_tag}{ideology}.tga')
            case 'default':
                copyfile(f'templates/flags/default.tga', f'{self.mod_path}/gfx/flags/{self.tag}_{cosmetic_tag}{ideology}.tga')
            case 'medium':
                copyfile(f'templates/flags/medium.tga', f'{self.mod_path}/gfx/flags/medium/{self.tag}_{cosmetic_tag}{ideology}.tga')
            case 'small':
                copyfile(f'templates/flags/small.tga', f'{self.mod_path}/gfx/flags/small/{self.tag}_{cosmetic_tag}{ideology}.tga')
                
        '''
        if ideology == 'all':
            for ideology in ideologies:
                match size:
                    case 'all':
                        copyfile(f'templates/flags/default.tga', f'{self.mod_path}/gfx/flags/{self.tag}_{cosmetic_tag}{ideology}.tga')
                        copyfile(f'templates/flags/medium.tga', f'{self.mod_path}/gfx/flags/medium/{self.tag}_{cosmetic_tag}{ideology}.tga')
                        copyfile(f'templates/flags/small.tga', f'{self.mod_path}/gfx/flags/small/{self.tag}_{cosmetic_tag}{ideology}.tga')
                    case 'default':
                        copyfile(f'templates/flags/default.tga', f'{self.mod_path}/gfx/flags/{self.tag}_{cosmetic_tag}{ideology}.tga')
                    case 'medium':
                        copyfile(f'templates/flags/medium.tga', f'{self.mod_path}/gfx/flags/medium/{self.tag}_{cosmetic_tag}{ideology}.tga')
                    case 'small':
                        copyfile(f'templates/flags/small.tga', f'{self.mod_path}/gfx/flags/small/{self.tag}_{cosmetic_tag}{ideology}.tga')
        '''
                
        messagebox.showinfo('Successs', 'You have successfully generated country flag/s')