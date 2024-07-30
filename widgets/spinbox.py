import customtkinter as ctk
class Spinbox(ctk.CTkFrame):
    def __init__(self,
                 parent,
                 fg_color="transparent",
                 corner_radius=0,
                 width=200,
                 height=45,
                 font=("Comfortaa",15),
                 step_size = 1,
                 type = int,
                 only_entry = False,
                 **kwargs):
        super().__init__(parent,fg_color=fg_color)

        self.step_size = step_size
        self.type = type

        # - #DBDBDB
        self.controls_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.controls_frame.pack()

        if not only_entry:
            self.minus_button = ctk.CTkButton(self.controls_frame, fg_color="white",bg_color="white",text="-",text_color="black",width=15, command=self.substract)
            self.minus_button.pack(side="left")

        self.entry = ctk.CTkEntry(self.controls_frame,border_width=0,bg_color="transparent",fg_color="white",width=width,height=height,font=font,corner_radius = corner_radius,**kwargs)
        self.entry.pack(side="left",fill="both",expand=True)

        if not only_entry:
            self.plus_button = ctk.CTkButton(self.controls_frame, fg_color="white",bg_color="white",text="+",text_color="black",width=15, command=self.add)
            self.plus_button.pack(side="right")

        self.lane = ctk.CTkFrame(self,fg_color="black",height=2,width=width)
        self.lane.pack()

    def convert_to_type(self,value):
        if self.type == int:
            value = int(value)
            return value
        elif self.type == float:
            return float(value)
        else:
            return value

    def add(self):
        try:
            value = self.convert_to_type(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def substract(self):
        try:
            value = self.convert_to_type(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return


    def set_focus(self):
        self.after(150, lambda: self.entry.focus())
    def bind(self,command):
        self.entry.bind("<Return>", command)
    def entry_value(self):
        return self.entry.get()
    def update_with_value(self, new_value):
        self.entry.delete(0, "end")
        self.entry.insert(0, new_value)
    def disable(self):
        self.entry.configure(state="disabled")