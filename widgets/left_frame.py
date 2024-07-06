import customtkinter as ctk
class LeftFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #DO skończenia def create_table(self):
        style = ttk.Style()
        style.configure("Treeview", font=("Comfortaa",11))
        style.configure("Treeview.Heading", font=("Comfortaa",15))

        self.left_frame = ctk.CTkFrame(self,fg_color="transparent")
        self.left_frame.pack(side="left",expand=True,fill="both")

        self.table = ttk.Treeview(self.left_frame,selectmode="browse",columns = ("from_account","person_name","amount","date","name","type"), show = "headings")
        self.table.heading("from_account", text=tr.translate("Numer konta"))
        self.table.heading("person_name", text=tr.translate("Imię osoby"))
        self.table.heading("amount", text=tr.translate("Kwota"))
        self.table.column("amount",width=75)
        self.table.heading("date", text=tr.translate("Data transakcji"))
        self.table.heading("name", text=tr.translate("Nazwa"))
        self.table.heading("type", text=tr.translate("Typ"))
        self.table.column("name",width=100)
        self.table.column("date",width=130)
        self.table.column("type",width=110)
        self.table.pack(fill = "both", expand = True,padx=10,pady=10)

        self.right_frame = ctk.CTkFrame(self,fg_color="transparent")
        self.right_frame.pack(side="right",expand=True,fill="both")

        self.centered_frame = ctk.CTkFrame(self.right_frame,fg_color="transparent")
        self.centered_frame.place(relx=0.5,rely=0.5,anchor="center")

        self.label = ctk.CTkLabel(self.centered_frame,text=tr.translate("Z wybranymi:"),font=("Comfortaa",25))
        self.label.pack(padx=10,pady=10)

        self.renew_button = BankButton(self.centered_frame,image = ImagesLoader.images["renew_icon"],text=tr.translate("Ponów"),command = self.renew_transaction,fg_color="orange")
        self.renew_button.pack(padx=10,pady=10)