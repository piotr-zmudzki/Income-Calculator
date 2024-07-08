import customtkinter as ctk
import main_font
from widgets import title_value_widget


class RightFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    
        self.center_frame = CenterTextFrame(self, fg_color = "transparent")
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")


class CenterTextFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = main_font.get_prefered_font()
        self.place_widgets()

    def place_widgets(self):
        label = ctk.CTkLabel(master=self, text="Google",font=self.font)
        label.pack(pady=10)

        label2 = ctk.CTkLabel(master=self, text="2Google",font=self.font)
        label2.pack(pady=10)

        test = title_value_widget.NameValueWidget(self,label_name= "Dzisiejszy przychód", value= -1.99)
        test.pack(pady=10)
        test.update_value(0.82)

    