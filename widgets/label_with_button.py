import customtkinter as ctk
import main_font
class LabelWithButton(ctk.CTkFrame):
    def __init__(self,parent,button_icon,button_side,text,command = None,fg_color="transparent",font = None,**kwargs):
        super().__init__(parent,fg_color=fg_color,**kwargs)
        if font is None:
            font = main_font.get_prefered_font()
        button = ctk.CTkButton(self,image = button_icon,text=None,fg_color="transparent",width=64,hover_color="#8c918d",command = command)
        button.pack(side=button_side)

        label = ctk.CTkLabel(self,text=text,font=font)
        label.pack(side=button_side)