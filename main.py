import customtkinter as ctk
import logging
import widgets
from datetime import datetime 


#imports constans from a local file
import constants
from widgets import right_frame, left_frame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.window_resolution = "1000x550"

        self.geometry(self.window_resolution)
        self.title(constants.APP_NAME)
        #custom_fonts.set_default_font()

        self.create_widgets()
    
    def create_widgets(self):
        self.left_frame = widgets.left_frame.LeftFrame(self)
        self.left_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        self.left_frame.add_data((1,17,"6.5zł",17,"Karta",datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        self.right_frame = widgets.right_frame.RightFrame(self)
        self.right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

def set_theme():
    #The theme will be set to "system" if wrong name provided
    #Avalible: "system", "light", "dark"
    ctk.set_appearance_mode(constants.THEME)


if __name__ == "__main__":
    set_theme()
    app = App()
    app.mainloop()