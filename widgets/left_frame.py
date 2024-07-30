import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from modules import data_manager, calculations
from widgets import custom_button, new_row_panel, notification
from PIL import Image
import globals
import logging

class LeftFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #place frame for buttons
        self.place_bottom_frame()

        style = ttk.Style()
        style.configure("Treeview", font=("Comfortaa",15))
        style.configure("Treeview.Heading", font=("Comfortaa",20))

        #create treeview (table)
        self.table = ttk.Treeview(self,selectmode="browse",columns = ("lp","qty","price_per_unit","gotten_money_amount","payment_type","date","time"), show = "headings")
        
        self.configure_table_headings()
        
        self.table.pack(fill = "both", expand = True,padx=10,pady=10)

        try:
            self.load_and_insert_data()
        except Exception as e:
            notification.Notification(self,f"Coś poszło nie tak\n(ładowanie danych)", "block")
            logging.critical(e)

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

        self.delete_entry_button = custom_button.CustomButton(self.bottom_frame, text="Usuń", image=delete_icon, fg_color="red", command = self.delete_item)
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
        #creates class instance (ctk.CTkToplevel)
        panel = new_row_panel.NewRowQuestionPanel()
        
        #disable buttons
        self.disable_buttons()

        #get user input from NewRowQuestionPanel
        tuple = panel.get_tuple()
        if len(tuple) == 0:
            self.enable_buttons()
            return False
        
        #enable buttons
        self.enable_buttons()
        
        #return user input from Toplevel
        return tuple
    
    #adds item both to the treeview and the database
    def add_item(self):
        tuple = self.open_new_panel()
        if not tuple:
            return
        
        #appends a row to the treeview
        self.add_data(tuple)

        #appends a row to the database
        data_manager.append_data([tuple])

        #sums new data
        calculations.Calculator.sum(tuple[3], tuple[5])
        globals.labels_need_refresh = 1

        notification.Notification(self,"Dodawanie zakończone","done")
    
    def edit_item(self):
        # Get selected item
        selected_item = self.table.selection()[0]
        row_number = self.table.item(self.table.focus())["values"][0]


        data_tuple = self.open_new_panel()
        if not data_tuple:
            return
        
        #modifying treeview is not necessary, because it wll be reloaded anyways
        #self.table.item(selected_item, values=data_tuple)
        
        #edit row in database
        data_manager.edit_row_from_database(row_number, data_tuple)

        # Set sums to 0
        calculations.Calculator.reset_variables()
        
        # Clear treeview and recalculate everything
        self.clear_treeview()
        self.load_and_insert_data()
        globals.labels_need_refresh = 1
    
        notification.Notification(self,"Edytowanie zakończone","done")
        
    def delete_item(self):
        if not notification.Notification(self,"Czy napewno?","ask",True).get_input():
            return


        selected_item = self.table.selection()[0]

        row_number = self.table.item(self.table.focus())["values"][0]
        income = self.table.item(self.table.focus())["values"][3]
        date = self.table.item(self.table.focus())["values"][5]

        # Delete row from treeview (table)
        self.table.delete(selected_item)

        # Modify the database
        data_manager.delete_row_from_database(row_number)

        calculations.Calculator.sum(income, date,deduct=True)
        globals.labels_need_refresh = 1
    
        notification.Notification(self,"Usuwanie zakończone","done")

    def clear_treeview(self):
        for item in self.table.get_children():
            self.table.delete(item)

    # Adds data to the treeview and sums data
    def load_and_insert_data(self):
        loaded_data = data_manager.load_data()
        for row in loaded_data:
            self.add_data(row)
            #                           income,  date
            calculations.Calculator.sum(row[3], row[5])
    
    # Updates the number (LP. ) of last_row
    # Useful in creating data tuple in new_row_panel
    def update_last_row_nr(self, value):
        try:
            globals.last_row_nr = int(value) + 1
        except UnboundLocalError:
            logging.critical("No rows")
            
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

        #configure style
        style = ttk.Style()
        style.configure("Treeview", 
                        background = "silver"
                )
        style.map("Treeview", background = [("selected", "#6c827b")])


        #configure treeview tags
        self.table.tag_configure("cost", background="#fa5252", foreground="white")
        self.table.tag_configure("income", background="#099c1f", foreground="white")
    
    #gets tag name based on income/cost
    def get_tag(self, income):
        if float(income) < 0:
            return "cost"
        else:
            return "income"

    def add_data(self, data_tuple: tuple):
        self.table.insert(parent = "", index = tk.END, values = (data_tuple), tags=(self.get_tag(data_tuple[3])))

        self.update_last_row_nr(data_tuple[0])