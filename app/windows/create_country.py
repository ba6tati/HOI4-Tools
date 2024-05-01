from customtkinter import *
from CTkColorPicker import AskColor
from colormap import hex2rgb, rgb2hex
from config import WINDOW_TITLE, WINDOW_SIZE

cultures = ('middle_eastern', 'eastern_european', 'western_european', 'african', 'asian', 'southamerican', 'commonwealth')

class CreateCountryWindow(CTkToplevel):
    def __init__(self, master, mod_path=None):
        super().__init__(master)
        
        self.title(WINDOW_TITLE + ' | Create Country')
        self.geometry(WINDOW_SIZE)
        
        self.frame = CTkFrame(self)
        
        
        self.mod_path = CTkEntry(self.frame, placeholder_text='Mod Path')
        
        if mod_path:
            self.mod_path.insert(0, mod_path)
        
        self.select_path_btn = CTkButton(self.frame, text='Select', command=self.select_directory)
        
        self.tag = CTkEntry(self.frame, placeholder_text='TAG')
        self.name = CTkEntry(self.frame, placeholder_text='Name')
        
        self.culture_lbl = CTkLabel(self.frame, text='Culture: ')
        self.culture = CTkOptionMenu(self.frame, values=cultures)
        
        self.color_lbl = CTkLabel(self.frame, text='Color:')
        self.color = CTkEntry(self.frame, placeholder_text='R G B', state='disabled')
        self.select_color_btn = CTkButton(self.frame, text='Select Color', command=self.select_color)
        
        self.generate_btn = CTkButton(self.frame, text='Generate', command=self.generate)
        
        self.mod_path.grid(row=0, column=0, columnspan=2)
        self.select_path_btn.grid(row=0, column=2)
        
        self.tag.grid(row=1, column=0, columnspan=3)
        self.name.grid(row=2, column=0, columnspan=3)
        self.culture_lbl.grid(row=3, column=0)
        self.culture.grid(row=3, column=1, columnspan=2)
        self.color_lbl.grid(row=4, column=0)
        self.color.grid(row=4, column=1)
        self.select_color_btn.grid(row=4, column=2)
        self.generate_btn.grid(row=5, column=0, columnspan=3)
            
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        for widget in self.frame.winfo_children():
            widget.grid_configure(padx=10, pady=10, sticky=NSEW)
        
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
            
    def generate(self):
        mod_path = self.mod_path.get()
        tag = self.tag.get()
        name = self.name.get()
        culture = self.culture.get()
        color = self.color.get()
        
        try:
            os.makedirs(f'{mod_path}/common/country_tags')
            os.makedirs(f'{mod_path}/countries')
        except FileExistsError:
            pass
        
        with open(f'{mod_path}/common/country_tags/{mod_path.split('/')[-1]}_countries.txt', 'a+') as f:
            f.write(f'\n{tag} = "countries/{name}.txt"')
        
        with open(f'templates/country.txt', 'r') as f:
            data = f.read()
            
        data = data.replace('#CULTURE#', culture).replace('#COLOR#', color)
        
        with open(f'{mod_path}/common/countries/{name}.txt', 'w+') as f:
            f.write(data)	
            
        with open(f'{mod_path}/common/countries/colors.txt', 'a+') as f:
            data = f"""\n{tag} = (
	color = rgb ( {color} )
	color_ui = rgb ( {color} )
)"""
            
            f.write(data.replace('(', '{').replace(')', '}'))
            
        self.tag.delete(0, END)
        self.name.delete(0, END)
        self.culture.set(cultures[0])
        self.color.delete(0, END)
        
if __name__ == '__main__':
    raise Exception('Run: python app/main.py')