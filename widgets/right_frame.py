import customtkinter as ctk
import main_font
from datetime import datetime
from widgets import title_value_widget
from modules import calculations
import threading
import time
import globals


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
        self.check_for_refresh_necessity()

    def check_for_refresh_necessity(self):
        self.refresh_thread = threading.Thread(target = self.check_for_refresh_necessity_loop,args=())
        self.refresh_thread.start()

    def check_for_refresh_necessity_loop(self):
        while True:
            time.sleep(1)
            print("checking...")
            if globals.labels_need_refresh == 1:
                print("needs refresh!")
                print(calculations.Calculator.general_sum)
                self.total_income_widget.update_value(calculations.Calculator.general_sum)
                self.today_gotten_money_widget.update_value(calculations.Calculator.today_income_sum)
                self.today_expenses_widget.update_value(calculations.Calculator.today_expenses_sum)
                self.today_income_widget.update_value(calculations.Calculator.today_general_sum)
                globals.labels_need_refresh = 0
                
    def place_widgets(self):
        self.total_income_widget = title_value_widget.NameValueWidget(self,label_name= "Całkowity dochód", value = calculations.Calculator.general_sum)
        self.total_income_widget.pack(pady=10)

        self.today_title = ctk.CTkLabel(self, text=f'- Dane z dzisiaj ({datetime.now().strftime("%Y-%m-%d")}) - ', font=ctk.CTkFont(family="Aptos Display", size=35))
        self.today_title.pack(pady=10)

        self.today_gotten_money_widget = title_value_widget.NameValueWidget(self, label_name="Dzisiejszy przychód", value = calculations.Calculator.today_income_sum)
        self.today_gotten_money_widget.pack(pady=10)

        self.today_expenses_widget = title_value_widget.NameValueWidget(self, label_name="Dzisiejsze koszty", value = calculations.Calculator.today_expenses_sum)
        self.today_expenses_widget.pack(pady=10)

        self.today_income_widget = title_value_widget.NameValueWidget(self, label_name="Dzisiejszy dochód", value = calculations.Calculator.today_general_sum)
        self.today_income_widget.pack(pady=10)

        

        #missing command! - how to communicate between two frames like that?
        
    