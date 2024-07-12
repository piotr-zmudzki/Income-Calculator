import customtkinter as ctk
from widgets import custom_button

class NewRowQuestionPanel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        self.qty_entry = ctk.CTkEntry(self, placeholder_text="Ilość")
        self.qty_entry.pack(padx=20, pady=10)

        self.price_per_unit_entry = ctk.CTkEntry(self, placeholder_text="Cena za szt")
        self.price_per_unit_entry.pack(padx=20, pady=10)

        self.income_entry = ctk.CTkEntry(self, placeholder_text="Przychód")
        self.income_entry.pack(padx=20, pady=10)

        self.type_entry = ctk.CTkEntry(self, placeholder_text="Typ")
        self.type_entry.pack(padx=20, pady=10)

        self.date_entry = ctk.CTkEntry(self, placeholder_text="Data")
        self.date_entry.pack(padx=20, pady=10)

        self.time_entry = ctk.CTkEntry(self, placeholder_text="Czas")
        self.time_entry.pack(padx=20, pady=10)

        self.finish_button = custom_button.CustomButton(self, text="Dodaj", command = self.finish, width=20, height=20)
        self.finish_button.pack(padx=20, pady=10)
    
    def finish(self):
        print("Finished")