from widgets import notification
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        #self.overrideredirect(True)

        self.button_1 = ctk.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = notification.Notification(self, "Czy michał się \nskichał?", "block", False)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
        print(self.toplevel_window.get_input())
app = App()
app.mainloop()

