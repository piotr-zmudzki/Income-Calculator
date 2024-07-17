import customtkinter as ctk
class Spinbox(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 200,
                 height: int = 32,
                 step_size = 1,
                 label_text = None,
                 type = int,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.label_text = label_text
        self.type = type

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        

        self.grid_columnconfigure((0, 2), weight=0, uniform = "a")  # buttons don't expand
        self.grid_columnconfigure(1, weight=1, uniform = "a")  # entry expands
        self.grid_rowconfigure((0,1), weight=0, uniform = "a")

        self.label = ctk.CTkLabel(self, text=self.label_text)
        self.label.grid(row = 0, column = 1, columnspan = 1)

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=1, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0, )
        self.entry.grid(row=1, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=1, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0.0")
        self.convert_to_type(1)
    def convert_to_type(self, value):
        self.type(2)


    def add_button_callback(self):
        try:
            value = self.convert_to_type(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> float:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(float(value)))