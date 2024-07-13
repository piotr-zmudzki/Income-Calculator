import customtkinter as ctk
import constants
from widgets import right_frame, left_frame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #set window resolution
        self.window_resolution = "1000x550"
        self.geometry(self.window_resolution)

        self.title(constants.APP_NAME)

        self.create_widgets()
    
    def create_widgets(self):
        self.left_frame = left_frame.LeftFrame(self)
        self.left_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        self.right_frame = right_frame.RightFrame(self)
        self.right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

def set_theme():
    #The theme will be set to "system" if wrong name provided
    #Avalible: "system", "light", "dark"
    ctk.set_appearance_mode(constants.THEME)


if __name__ == "__main__":
    set_theme()
    app = App()
    app.mainloop()