import customtkinter as ctk
import main_font
from datetime import datetime
from widgets import title_value_widget
from modules import calculations
from PIL import Image
#test
from widgets import left_frame


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
        total_income_widget = title_value_widget.NameValueWidget(self,label_name= "Całkowity dochód", value = calculations.Calculator.general_sum)
        total_income_widget.pack(pady=10)

        today_title = ctk.CTkLabel(self, text=f'- Dane z dzisiaj ({datetime.now().strftime("%Y-%m-%d")}) - ', font=ctk.CTkFont(family="Aptos Display", size=35))
        today_title.pack(pady=10)

        today_gotten_money_widget = title_value_widget.NameValueWidget(self, label_name="Dzisiejszy przychód", value = calculations.Calculator.today_income_sum)
        today_gotten_money_widget.pack(pady=10)

        today_expenses_widget = title_value_widget.NameValueWidget(self, label_name="Dzisiejsze koszty", value = calculations.Calculator.today_expenses_sum)
        today_expenses_widget.pack(pady=10)

        today_income_widget = title_value_widget.NameValueWidget(self, label_name="Dzisiejszy dochód", value = calculations.Calculator.today_general_sum)
        today_income_widget.pack(pady=10)

        

        #missing command! - how to communicate between two frames like that?
        
    