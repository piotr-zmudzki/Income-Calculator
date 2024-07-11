import customtkinter as ctk

class CustomButton(ctk.CTkButton):
    def __init__(self,parent,fg_color=None,text_color="white",width=200,height=85,font=("Product Sans",30),corner_radius = 100,**kwargs):
        if fg_color is None:
            fg_color="#1c56ad"
        super().__init__(parent,border_color=fg_color,fg_color="#f7f3f2",hover_color="#8c918d",border_width=5,text_color="black",width=width,height=height,font=font,corner_radius = corner_radius,**kwargs)
