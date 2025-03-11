from customtkinter import CTkButton

class Btn7(CTkButton):
        color = "#2E073F"
        hover_color = "#7A1CAC"
        digi_font = ("Bell MT", 25 , "bold")

        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs, fg_color=self.color,
                             corner_radius=5,
                             hover_color=self.hover_color,
                             font=self.digi_font,
                             text="7"
                             )