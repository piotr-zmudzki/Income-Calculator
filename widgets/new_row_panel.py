import customtkinter as ctk
from widgets import custom_button
from globals import last_row_nr
from datetime import datetime

class NewRowQuestionPanel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_row_tuple = ()
        self.geometry("500x300")

        self.lift()
        self.attributes("-topmost", True)
        self.after(10, self.create_widgets)
    def create_widgets(self):
        self.qty_entry = ctk.CTkEntry(self, placeholder_text="Ilość")
        self.qty_entry.pack(padx=20, pady=10)

        self.price_per_unit_entry = ctk.CTkEntry(self, placeholder_text="Cena za szt")
        self.price_per_unit_entry.pack(padx=20, pady=10)

        self.income_entry = ctk.CTkEntry(self, placeholder_text="Przychód")
        self.income_entry.pack(padx=20, pady=10)

        self.type_entry = ctk.CTkEntry(self, placeholder_text="Typ")
        self.type_entry.pack(padx=20, pady=10)

        """ 
        self.date_entry = ctk.CTkEntry(self, placeholder_text="Data")
        self.date_entry.pack(padx=20, pady=10)

        self.time_entry = ctk.CTkEntry(self, placeholder_text="Czas")
        self.time_entry.pack(padx=20, pady=10)"""

        self.finish_button = custom_button.CustomButton(self, text="Dodaj", command = self.finish, width=20, height=20)
        self.finish_button.pack(padx=20, pady=10)
    def get_tuple(self):
        self.wait_window(self)
        return self.new_row_tuple

    def finish(self):
        date_today = datetime.now().strftime("%d-%m-%Y")
        time_today = datetime.now().strftime("%H:%M:%S")
        self.new_row_tuple = (last_row_nr,self.qty_entry.get(),self.price_per_unit_entry.get(),self.income_entry.get(),self.type_entry.get(),date_today,
                              time_today)
        self.destroy()
        self.update()
