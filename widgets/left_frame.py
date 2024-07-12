import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from modules import data_manager, calculations
from widgets import custom_button, new_row_panel
from PIL import Image

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

        add_entry_button = custom_button.CustomButton(self.bottom_frame, text="Dodaj", image=plus_icon, fg_color="green", command=self.add_item)
        add_entry_button.pack(pady=20, padx=10, side="left")

        edit_icon = ctk.CTkImage(light_image=Image.open("images/edit_icon.png"),
                                  size=(30, 30))

        edit_entry_button = custom_button.CustomButton(self.bottom_frame, text="Edytuj", image=edit_icon, fg_color="yellow")
        edit_entry_button.pack(pady=20, padx=10, side="left")

        delete_icon = ctk.CTkImage(light_image=Image.open("images/delete_icon.png"),
                                  size=(30, 30))

        delete_entry_button = custom_button.CustomButton(self.bottom_frame, text="Usuń", image=delete_icon, fg_color="red")
        delete_entry_button.pack(pady=20, padx=10, side="left")
    #This section applies to buttons only 
    def add_item(self):
        new_row_panel.NewRowQuestionPanel()
        #self.add_data(data_tuple)
        #data_manager.append_data([data_tuple])
    
    def edit_item(self, data_tuple: tuple):
        pass

    def load_and_insert_data(self):
        loaded_data = data_manager.load_data()
        for row in loaded_data:
            self.add_data(row)
            calculations.sum(row[3], row[5])
        print(calculations.general_sum)
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