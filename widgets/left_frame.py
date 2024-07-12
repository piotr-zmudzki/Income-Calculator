import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from modules import data_manager, calculations
from widgets import custom_button, new_row_panel
from PIL import Image
import globals
import logging

class LeftFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.place_bottom_frame()

        style = ttk.Style()
        style.configure("Treeview", font=("Comfortaa",15))
        style.configure("Treeview.Heading", font=("Comfortaa",20))

        #self.left_frame = ctk.CTkFrame(self,fg_color="transparent")
        #self.left_frame.pack(side="left",expand=True,fill="both")

        self.table = ttk.Treeview(self,selectmode="browse",columns = ("lp","qty","price_per_unit","gotten_money_amount","payment_type","date","time"), show = "headings")
        
        self.configure_table_headings()
        
        self.table.pack(fill = "both", expand = True,padx=10,pady=10)
        
        self.load_and_insert_data()

    def place_bottom_frame(self):
        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        plus_icon = ctk.CTkImage(light_image=Image.open("images/add_icon.png"),
                                  size=(30, 30))

        self.add_entry_button = custom_button.CustomButton(self.bottom_frame, text="Dodaj", image=plus_icon, fg_color="green", command=self.add_item)
        self.add_entry_button.pack(pady=20, padx=10, side="left")

        edit_icon = ctk.CTkImage(light_image=Image.open("images/edit_icon.png"),
                                  size=(30, 30))

        self.edit_entry_button = custom_button.CustomButton(self.bottom_frame, text="Edytuj", image=edit_icon, fg_color="yellow", command = self.edit_item)
        self.edit_entry_button.pack(pady=20, padx=10, side="left")

        delete_icon = ctk.CTkImage(light_image=Image.open("images/delete_icon.png"),
                                  size=(30, 30))

        self.delete_entry_button = custom_button.CustomButton(self.bottom_frame, text="Usuń", image=delete_icon, fg_color="red")
        self.delete_entry_button.pack(pady=20, padx=10, side="left")
    #This section applies to buttons only 
    def disable_buttons(self):
        self.add_entry_button.configure(state = "disabled")
        self.edit_entry_button.configure(state = "disabled")
        self.delete_entry_button.configure(state = "disabled")

    def enable_buttons(self):
        self.add_entry_button.configure(state = "enabled")
        self.edit_entry_button.configure(state = "enabled")
        self.delete_entry_button.configure(state = "enabled")

    def open_new_panel(self):
        panel = new_row_panel.NewRowQuestionPanel()
        self.disable_buttons()
        tuple = panel.get_tuple()
        if len(tuple) == 0:
            self.enable_buttons()
            return False
        self.enable_buttons()
        return tuple
    
    def add_item(self):
        tuple = self.open_new_panel()
        if not tuple:
            return
        self.add_data(tuple)
        data_manager.append_data([tuple])

        calculations.Calculator.sum(tuple[3], tuple[5])
        globals.labels_need_refresh = 1
    
    def edit_item(self):
        # Get selected item to Edit
        selected_item = self.table.selection()[0]
        row_number = self.table.item(self.table.focus())["values"][0]
        print(row_number)
        data_tuple = self.open_new_panel()
        if not data_tuple:
            return
        self.table.item(selected_item, values=data_tuple)
        
        data_manager.edit_row_from_database(row_number, data_tuple)

    def load_and_insert_data(self):
        loaded_data = data_manager.load_data()
        for row in loaded_data:
            self.add_data(row)
            calculations.Calculator.sum(row[3], row[5])
        
    def update_last_row_nr(self, value):
        try:
            globals.last_row_nr = int(value) + 1
        except UnboundLocalError:
            logging.critical("Now row to add, setting to default")
            
    def configure_table_headings(self):
        #configure headings names
        self.table.heading("lp", text="LP.")
        self.table.heading("qty", text="Ilość")
        self.table.heading("price_per_unit", text="Cena /szt")
        self.table.heading("gotten_money_amount", text="Przychód [zł]")
        self.table.heading("payment_type", text="Typ")
        self.table.heading("date", text="Data")
        self.table.heading("time", text="Godzina")
        
        #configure columns' other settings
        self.table.column("lp",width=25)
        self.table.column("qty",width=35)
        self.table.column("price_per_unit",width=70)
        self.table.column("gotten_money_amount",width=100)
        self.table.column("payment_type",width=100)
        self.table.column("date",width=145)
        self.table.column("time",width=100)

    def add_data(self, data_tuple: tuple):
        self.table.insert(parent = "", index = tk.END, values = (data_tuple))

        self.update_last_row_nr(data_tuple[0])