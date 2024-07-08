#this will be a widget that provides a name (const) and a value (variable)
#something like this:
# Income generated in this month (name): [red] -145.43zł (variable)
# additional argument: variable_color
# additional func: variable_update - which will re-set the variable part so it get's refreshed
import customtkinter as ctk
import main_font

class NameValueWidget(ctk.CTkFrame):
    def __init__(self, master, label_name, value, value_color = None, **kwargs):
        super().__init__(master, **kwargs)

        self.font = main_font.get_prefered_font()
        self.label_name = label_name
        self.value = value
        self.value_color = value_color

        self.place_widgets()

    def place_widgets(self):
        self.label1 = ctk.CTkLabel(self, text = f"{self.label_name}: ", font = self.font)
        self.label1.pack(side="left")

        self.value_label = ctk.CTkLabel(self, text = self.value, font = self.font, text_color=self.get_value_color(self.value))
        self.value_label.pack(side="left")

    def get_value_color(self, value_to_check):
        print(self.value_color)
        if self.value_color is None:
            if isinstance(value_to_check, int) or isinstance(value_to_check, float):
                if value_to_check < 0:
                    return "red"
                elif value_to_check == 0:
                    return "blue"
                else:
                    return "green"
            else:
                return "black"
        else:
            return self.value_color
    
    def update_value(self, new_value):
        self.value_label.configure(text_color = self.get_value_color(new_value), text=new_value)
