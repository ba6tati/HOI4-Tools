from customtkinter import *
from CTkColorPicker import AskColor
from colormap import hex2rgb, rgb2hex
from ctkcomponents import *

from config import WINDOW_TITLE, WINDOW_SIZE
from app.windows.create_flag import CreateFlag
from app.utils import make_directory_if_not_exists
from app.utils import open_window

cultures = ('middle_eastern', 'eastern_european', 'western_european', 'african', 'asian', 'southamerican', 'commonwealth')

class CreateCountryWindow(CTkToplevel):
    def __init__(self, master, mod_path=None):
        super().__init__(master)
        
        self.mod_path = mod_path
        
        self.validation = StringVar()
        
        self.title(WINDOW_TITLE + ' | Create Country')
        self.geometry(WINDOW_SIZE)
        
        self.frame = CTkFrame(self)
        
        self.validation_lbl = CTkLabel(self, textvariable=self.validation)
        
        self.tag = CTkEntry(self.frame, placeholder_text='TAG')
        
        self.name = CTkEntry(self.frame, placeholder_text='Name')
        
        self.culture_lbl = CTkLabel(self.frame, text='Culture: ')
        self.culture = CTkOptionMenu(self.frame, values=cultures)
        
        self.color_lbl = CTkLabel(self.frame, text='Color:')
        self.color = CTkEntry(self.frame, placeholder_text='R G B', state='disabled')
        self.select_color_btn = CTkButton(self.frame, text='Select Color', command=self.select_color)
        
        self.create_history_btn = CTkButton(self.frame, text='Create History File', command=self.create_history)
        self.create_flag_btn = CTkButton(self.frame, text='Create Flag', command=self.create_flag)
        self.create_character_btn = CTkButton(self.frame, text='Create Character', command=self.create_character)
        
        self.generate_btn = CTkButton(self.frame, text='Create', command=self.create)
        
        for widget in self.frame.winfo_children():
            widget.grid_configure(padx=10, pady=10, sticky=NSEW)
        
        self.validation_lbl.place(relx=0.5, rely=0.07, anchor=CENTER)
        self.tag.grid(row=1, column=0, columnspan=3)
        self.name.grid(row=2, column=0, columnspan=3)
        self.culture_lbl.grid(row=3, column=0)
        self.culture.grid(row=3, column=1, columnspan=2)
        self.color_lbl.grid(row=4, column=0)
        self.color.grid(row=4, column=1)
        self.select_color_btn.grid(row=4, column=2)
        self.create_history_btn.grid(row=5, column=0)
        self.create_flag_btn.grid(row=5, column=1)
        self.create_character_btn.grid(row=5, column=2)
        self.generate_btn.grid(row=6, column=0, columnspan=3)
        
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
        self.tag.bind('<FocusOut>', self.validate_tag)
        self.name.bind('<FocusOut>', self.validate_name)
        
    def select_color(self):
        initial_color = '#ffffff'
        if self.color.get():
            initial_color = rgb2hex(int(self.color.get().split()[0]), int(self.color.get().split()[1]), int(self.color.get().split()[2])).lower()
        
        color = AskColor(initial_color=initial_color)
        color = hex2rgb(color.get())
        
        self.color.configure(state='normal')
        self.color.delete(0, END)
        self.color.insert(0, color)
        self.color.configure(state='disabled')
        
        self.after(10, self.lift)
        
    def select_directory(self):
        mod_path = filedialog.askdirectory()
        
        if mod_path:
            self.mod_path.delete(0, END)
            self.mod_path.insert(0, mod_path)
            
    def validate(self):
        self.validate_name()
        self.validate_tag()
            
    def create(self):
        self.validate()
        
        if self.validation.get() == '':
            tag = self.tag.get()
            name = self.name.get()
            culture = self.culture.get()
            color = self.color.get()
            
            make_directory_if_not_exists(f'{self.mod_path}/common/country_tags')
            make_directory_if_not_exists(f'{self.mod_path}/common/countries')
            
            with open(f'{self.mod_path}/common/country_tags/{self.mod_path.split('/')[-1]}_countries.txt', 'a+') as f:
                f.write(f'\n{tag} = "countries/{name}.txt"')
            
            with open(f'templates/country.txt', 'r') as f:
                data = f.read()
                
            data = data.replace('#CULTURE#', culture).replace('#COLOR#', color)
            
            with open(f'{self.mod_path}/common/countries/{name}.txt', 'w+') as f:
                f.write(data)	
                
            with open(f'{self.mod_path}/common/countries/colors.txt', 'a+') as f:
                data = f"""\n{tag} = (\n\tcolor = rgb ( {color} )\n\tcolor_ui = rgb ( {color} )\n)"""
                
                f.write(data.replace('(', '{').replace(')', '}'))
                
            self.tag.delete(0, END)
            self.name.delete(0, END)
            self.culture.set(cultures[0])
            self.color.delete(0, END)
    
    def validate_tag(self, event=None):
        if len(self.tag.get()) != 3:
            self.validation.set('The TAG must be 3 characters long')
        else:
            self.validation.set('')
    
    def validate_name(self, event=None):
        if len(self.name.get()) < 1:
            self.validation.set('The country name must be at least 1 character long')
        else:
            self.validation.set('')
            
    def create_history(self):
        pass
        
    def create_flag(self):
        open_window(self, CreateFlag, mod_path=self.mod_path, tag=self.tag)
            
    def create_character(self):
        pass
    
if __name__ == '__main__':
    raise Exception('Run: python app/main.py')