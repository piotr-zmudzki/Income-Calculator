import customtkinter as ctk
import logging

#imports constans from a local file
import constants


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.window_resolution = "1000x550"

        self.geometry(self.window_resolution)
        self.title(constants.APP_NAME)
    
    def create_widgets(self):
        pass

def set_theme():
    #The theme will be set to "system" if wrong name provided
    #Avalible: "system", "light", "dark"
    ctk.set_appearance_mode(constants.THEME)


if __name__ == "__main__":
    set_theme()
    app = App()
    app.mainloop()