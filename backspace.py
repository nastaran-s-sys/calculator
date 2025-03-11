from customtkinter import CTkButton

class Backspace(CTkButton):
    color = "black"
    hover_color = "#7A1CAC"
    digi_font = ("Times New Roman (Headings CS)", 20)
    def __init__(self , master, **kwargs):
        super().__init__(master, **kwargs ,
                         fg_color = self.color,
                         corner_radius = 5,
                         hover_color = self.hover_color,
                         font = self.digi_font
                         )