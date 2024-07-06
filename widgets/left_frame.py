import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class LeftFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #DO skończenia def create_table(self):
        style = ttk.Style()
        style.configure("Treeview", font=("Comfortaa",15))
        style.configure("Treeview.Heading", font=("Comfortaa",20))

        #self.left_frame = ctk.CTkFrame(self,fg_color="transparent")
        #self.left_frame.pack(side="left",expand=True,fill="both")

        self.table = ttk.Treeview(self,selectmode="browse",columns = ("lp","qty","price_per_unit","gotten_money_amount","payment_type","date"), show = "headings")
        
        self.configure_table_headings()

        self.table.pack(fill = "both", expand = True,padx=10,pady=10)
        self.add_data((1,2,3,"nigdy",5,6))

    def configure_table_headings(self):
        self.table.heading("lp", text="LP.")
        self.table.heading("qty", text="Ilość")
        self.table.heading("price_per_unit", text="Cena /szt")
        #self.table.column("amount",width=75)
        self.table.heading("gotten_money_amount", text="Przychód")
        self.table.heading("payment_type", text="Metoda transakcji")
        self.table.heading("date", text="Czas")
        #self.table.column("name",width=100)
        #self.table.column("date",width=130)
        #self.table.column("type",width=110)

    def add_data(self, data_tuple):
        self.table.insert(parent = "", index = tk.END, values = (data_tuple))