from customtkinter import *
from tkinter import *
from tkinter import messagebox
from CTkDataVisualizingWidgets import *
from datetime import datetime
from shutil import copyfile
from config import WINDOW_TITLE, WINDOW_SIZE
from app.utils import toggle_widget, make_directory_if_not_exists

ideologies = ('democratic', 'communism', 'fascism', 'neutrality')

class CreateHistory(CTkToplevel):
    
    def __init__(self, master: CTk, mod_path, tag, country_name):
        
        super().__init__(master)
        
        self.title(WINDOW_TITLE + ' | Create History File')
        
        self.geometry(WINDOW_SIZE)
        
        self.mod_path = mod_path
        self.tag = tag
        self.country_name = country_name
        
        self.main_frame = CTkFrame(self)
        
        self.capital_lbl = CTkLabel(self.main_frame, text='Capital:')
        self.capital = CTkEntry(self.main_frame, placeholder_text='STATE ID')
        
        self.research_slots_lbl = CTkLabel(self.main_frame, text='Research slots:')
        self.research_slots = CTkEntry(self.main_frame, placeholder_text='Research slots')
        self.research_slots.insert(0, "1") 
        
        self.stability_lbl = CTkLabel(self.main_frame, text='Stability:')
        self.stability = CTkEntry(self.main_frame, placeholder_text='Stability')
        self.stability.insert(0, "0.5")
        
        self.war_support_lbl = CTkLabel(self.main_frame, text='War Support:')
        self.war_support = CTkEntry(self.main_frame, placeholder_text='War Support')
        self.war_support.insert(0, "0.5")
        
        self.communism_lbl = CTkLabel(self.main_frame, text='Communism:')
        self.communism = CTkEntry(self.main_frame, placeholder_text='Communism')
        self.communism.insert(0, "25")
        
        self.democratic_lbl = CTkLabel(self.main_frame, text='Democratic:')
        self.democratic = CTkEntry(self.main_frame, placeholder_text='Democratic')
        self.democratic.insert(0, "25")
        
        self.fascism_lbl = CTkLabel(self.main_frame, text='Fascism:')	
        self.fascism = CTkEntry(self.main_frame, placeholder_text='Fascism')
        self.fascism.insert(0, "25")
        
        self.neutrality_lbl = CTkLabel(self.main_frame, text='Neutrality:')
        self.neutrality = CTkEntry(self.main_frame, placeholder_text='Neutrality')
        self.neutrality.insert(0, "25")
        
        self.ruling_pary_lbl = CTkLabel(self.main_frame, text='Ruling Party:')
        self.ruling_pary = CTkComboBox(self.main_frame, values=ideologies)
        
        #self.election_allowed_lbl = CTkLabel(self.main_frame, text='Election Allowed:')
        self.election_allowed = CTkCheckBox(self.main_frame, text='Election Allowed')
        self.election_frequency_lbl = CTkLabel(self.main_frame, text='Election Frequency:')
        self.election_frequency = CTkEntry(self.main_frame, placeholder_text='Election Frequency')
        self.election_frequency.insert(0, "48")
        
        
        
        self.generate_button = CTkButton(self.main_frame, text='Generate', command=self.generate)
        
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.capital_lbl.grid(row=0, column=0, columnspan=2)
        self.capital.grid(row=0, column=2, columnspan=2)
        
        self.research_slots_lbl.grid(row=1, column=0, columnspan=2)
        self.research_slots.grid(row=1, column=2, columnspan=2)
        
        self.stability_lbl.grid(row=2, column=0)
        self.stability.grid(row=2, column=1)
        
        self.war_support_lbl.grid(row=2, column=2)
        self.war_support.grid(row=2, column=3)
        
        self.communism_lbl.grid(row=3, column=0)
        self.communism.grid(row=3, column=1)
        self.democratic_lbl.grid(row=3, column=2)
        self.democratic.grid(row=3, column=3)
        self.fascism_lbl.grid(row=4, column=0)
        self.fascism.grid(row=4, column=1)
        self.neutrality_lbl.grid(row=4, column=2)
        self.neutrality.grid(row=4, column=3)
        
        self.ruling_pary_lbl.grid(row=5, column=0, columnspan=2)
        self.ruling_pary.grid(row=5, column=2, columnspan=2)
        
        self.election_allowed.grid(row=6, column=0)
        
        self.election_frequency_lbl.grid(row=6, column=2)
        self.election_frequency.grid(row=6, column=3)
        
        self.generate_button.grid(row=8, column=0, columnspan=4)
        
        #self.election_allowed.bind('<Button-1>', command=print('BMB')) # TODO: doesnt work
        
        for widget in self.main_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10, sticky=NSEW)
        
    def generate(self):
        capital = self.capital.get()
        research_slots = self.research_slots.get()
        stability = self.stability.get()
        war_support = self.war_support.get()
        communism = self.communism.get()
        democratic = self.democratic.get()
        fascism = self.fascism.get()
        neutrality = self.neutrality.get()
        ruling_party = self.ruling_pary.get()
        
        if self.election_allowed.get():
            election_allowed = 'yes'
        else:
            election_allowed = 'no'
            
        election_frequency = self.election_frequency.get()
        
        file_name = f'{self.tag} - {self.country_name}'
        
        make_directory_if_not_exists(f'{self.mod_path}/history/countries')
        
        with open('templates/country_history.txt', 'r') as f:
            data = f.read()
            
        data = data.replace('#DEMOCRATIC#', democratic).replace('#FASCISM#', fascism).replace('#NEUTRALITY#', neutrality).replace('#RULING_PARTY#', ruling_party).replace('#ELECTIONS_ALLOWED#', election_allowed).replace('#ELECTION_FREQUENCY#', election_frequency).replace('#COMMUNISM#', communism).replace('#WAR_SUPPORT#', war_support).replace('#STABILITY#', stability).replace('#TAG#', str(self.tag)).replace('#CAPITAL#', capital).replace('#RESEARCH_SLOTS#', research_slots)
    
        with open(f'{self.mod_path}/history/countries/{file_name}.txt', 'w+') as f:
            f.write(data)
        
        messagebox.showinfo('Successs', 'You have successfully created country history file')
        
        self.capital.delete(0, END)
        
        self.research_slots.delete(0, END)
        self.research_slots.insert(0, "1")
        
        self.stability.delete(0, END)
        self.stability.insert(0, "0.5")
        
        self.war_support.delete(0, END)
        self.war_support.insert(0, "0.5")
        
        self.communism.delete(0, END)
        self.communism.insert(0, "25")
        
        self.democratic.delete(0, END)
        self.democratic.insert(0, "25")
    
        self.fascism.delete(0, END)
        self.fascism.insert(0, "25")
        
        self.neutrality.delete(0, END)
        self.neutrality.insert(0, "25")
        
        self.election_frequency.delete(0, END)
        self.election_frequency.insert(0, "48")