import customtkinter as ctk
from widgets import custom_button, spinbox
import globals
import tkinter
from datetime import datetime
from PIL import Image

class NewRowQuestionPanel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_row_tuple = ()
        self.geometry("900x600")
        self.maxsize(900,890)
        self.minsize(550,550)

        print("new row", globals.last_row_nr)
        
        self.bg_image = ctk.CTkImage(light_image=Image.open("images/gradient.png"),
                                  size=(900,900))
        
        self.box_plus_image = ctk.CTkImage(light_image=Image.open("images/box_plus_icon.png"),
                                  size=(50,50))
        

        self.lift()
        self.attributes("-topmost", True)
        #self.after(10, self.create_widgets)
        self.create_widgets()

    def create_widgets(self):
        self.background = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.background.place(x=0, y=0)

        self.center_frame = ctk.CTkFrame(self,width=520, height=520,bg_color="white",fg_color="white",border_color="gray",border_width=0)
        self.center_frame.place(relx=0.5, rely=0.5, anchor = "center")

        self.center_frame.pack_propagate(0)  #make frame not shrink to fit

        self.income_segmented_button = ctk.CTkSegmentedButton(self.center_frame,
                                                     values=["Wydatek (-)","Wpływ (+)"],
                                                     command=None, selected_color="#f59a95", text_color="black", font=("Product Sans", 25), selected_hover_color="#fd5bde")
        self.income_segmented_button.pack(pady=5)
        self.income_segmented_button.set("Wpływ (+)")  # set initial value

        self.qty_label = ctk.CTkLabel(self.center_frame, text="Ilość")
        self.qty_label.pack(pady=5)

        self.qty_textvar = tkinter.StringVar(value="1")
        self.qty_textvar.trace_add("write", self.update_income_entry)

        self.qty_spinbox = spinbox.Spinbox(self.center_frame, placeholder_text = "Ilość", textvariable = self.qty_textvar)
        self.qty_spinbox.pack(padx = 10, pady=5)

        self.price_textvar = tkinter.StringVar(value="1")
        self.price_textvar.trace_add("write", self.update_income_entry)

        self.price_label = ctk.CTkLabel(self.center_frame, text="Cena za sztukę")
        self.price_label.pack(pady=5)

        self.price_per_unit_entry = spinbox.Spinbox(self.center_frame, placeholder_text = "Cena za szt", type=float, step_size=0.5, textvariable = self.price_textvar)
        self.price_per_unit_entry.pack(padx = 10, pady=5)

        self.income_label = ctk.CTkLabel(self.center_frame, text="Przychód")
        self.income_label.pack(pady=5)

        self.income_entry = spinbox.Spinbox(self.center_frame, placeholder_text = "Przychód", only_entry=True)
        self.income_entry.pack(pady=5, padx=10)

        self.type_entry = spinbox.Spinbox(self.center_frame, placeholder_text = "Typ/ Nazwa", only_entry=True)
        self.type_entry.pack(padx=10, pady=10)

        self.finish_button = custom_button.CustomButton(self.center_frame,image=self.box_plus_image ,text="Dodaj", command = self.finish, width=20, height=20)
        self.finish_button.pack(padx=20, pady=5)

    def update_income_entry(self, *useless):
        self.income_entry.update_with_value(float(self.price_textvar.get())*float(self.qty_textvar.get()))

    def get_tuple(self):
        self.wait_window(self)
        return self.new_row_tuple

    def finish(self):
        date_today = datetime.now().strftime("%d-%m-%Y")
        time_today = datetime.now().strftime("%H:%M:%S")
        if self.income_segmented_button.get() == "Wydatek (-)":
            income = float(self.income_entry.entry_value()) * (-1)
        else:
            income = self.income_entry.entry_value()
        print(globals.last_row_nr)
        self.new_row_tuple = (globals.last_row_nr,self.qty_spinbox.entry_value(),self.price_per_unit_entry.entry_value(),income,self.type_entry.entry_value(),date_today,
                              time_today)
        self.destroy()
        self.update()
