import customtkinter as ctk
from PIL import Image
import winsound
import threading
import time


class Notification(ctk.CTkToplevel):
    def __init__(self, master, notify_text="Some text", icon_type="alert", question_mode = False, flashing_mode = False, *args, **kwargs):
        super().__init__(master,*args, **kwargs)
        self.geometry("300x180")
        self.title("Powiadomienie")
        self.resizable(False,False)
        #self.overrideredirect(True)
        self.attributes("-toolwindow", 1)
        self.attributes("-topmost", True)

        self.notify_text = notify_text
        self.icon_type = icon_type
        self.question_mode = question_mode
        self.flashing_mode = flashing_mode

        self.play_sound()
        self.load_images()
        self.place_widgets()

        if self.flashing_mode:
            self.flashing_thread = threading.Thread(target = self.turn_on_flashing,args=())
            self.flashing_thread.start()
        
    def play_sound(self):
        if self.question_mode:
            winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
        else:
            winsound.PlaySound("SystemHand", winsound.SND_ASYNC)
    def load_images(self):
        self.alert_icon = ctk.CTkImage(light_image=Image.open("images/alert_icon.ico"),
                                  size=(64,64))
        
        self.info_icon = ctk.CTkImage(light_image=Image.open("images/info_icon.ico"),
                                  size=(64,64))
        
        self.block_icon = ctk.CTkImage(light_image=Image.open("images/block_icon.ico"),
                                  size=(64,64))
        
        self.done_icon = ctk.CTkImage(light_image=Image.open("images/done_icon.ico"),
                                  size=(64,64))
        
        self.ask_icon = ctk.CTkImage(light_image=Image.open("images/ask_icon.ico"),
                                  size=(64,64))
    
    def get_text_color(self):
        if self.icon_type == "alert":
            return "#fcba03"  #yellow
        elif self.icon_type == "block":
            return "red"
        elif self.icon_type == "info" or self.icon_type == "ask":
            return "#4287f5"  #light blue
        elif self.icon_type == "done":
            return "green"
        else:
            return "black"

    def return_and_destroy(self, to_return):
        self.to_return = to_return
        self.destroy()
        self.update()
        
    def get_input(self) -> bool:
        self.wait_window()
        try:
            return self.to_return
        except AttributeError:
            return True
    
    def turn_on_flashing(self):
        time.sleep(0.5)
        while self.winfo_exists():
            self.icon_widget.pack_forget()
            time.sleep(0.5)
            self.icon_widget.pack()
            time.sleep(0.5)

    def place_widgets(self):
        self.left_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.left_frame.pack(side="left", padx=10)

        self.icon_widget = ctk.CTkLabel(self.left_frame, text="", image=eval(f"self.{self.icon_type}_icon"))
        self.icon_widget.pack()

        self.right_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.right_frame.pack(side="left",fill="both", expand=True, padx=10, pady=20)

        self.label = ctk.CTkLabel(self.right_frame, text="Uwaga!", font = ("Cascadia Code", 30), text_color=self.get_text_color())
        self.label.pack()

        self.label2 = ctk.CTkLabel(self.right_frame, text=self.notify_text, font = ("Cascadia Code", 15))
        self.label2.pack()

        if self.question_mode:
            self.place_yes_no_buttons()
        else:
            self.place_ok_button()

    def place_ok_button(self):
        self.ok_button = ctk.CTkButton(self.right_frame, text="OK", corner_radius=0,border_width=0,hover_color="gray",fg_color="black",text_color="white",
                                       command=self.destroy, width=100, font=("Yu Gothic", 15))
        self.ok_button.pack(side="bottom",pady=10)

    def place_yes_no_buttons(self):
        self.btn_frame = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        self.btn_frame.pack(side="bottom",pady=10)

        self.yes_button = ctk.CTkButton(self.btn_frame,text="Tak", corner_radius=0,border_width=0,hover_color="green",fg_color="black",text_color="white",
                                       command=lambda: self.return_and_destroy(True), width=70, font=("Yu Gothic", 15))
        self.yes_button.pack(side="left",padx=5,fill="both",expand=True)

        self.no_button = ctk.CTkButton(self.btn_frame,text="Nie", corner_radius=0,border_width=0,hover_color="red",fg_color="black",text_color="white",
                                       command=lambda: self.return_and_destroy(False), width=70, font=("Yu Gothic", 15))
        self.no_button.pack(side="left",padx=5,fill="both",expand=True)
