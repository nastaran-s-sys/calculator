from customtkinter import CTkEntry
# from customtkinter import *

class Entry(CTkEntry):
    color = "transparent"
    digi_font = ("Bell MT", 25, "bold")
    def __init__(self, master, **kwargs):
        CTkEntry.__init__(self, master, **kwargs , fg_color= self.color , border_width= 0 , font = self.digi_font)

# app = CTk()
# def press(key):
#     entry.insert(END, key)
# def calculate():
#     try:
#         num = entry.get()
#         result = eval(num)
#         entry.delete(0, END)
#         entry.insert(0, str(f"{num} = {result}"))
#     except:
#         entry.delete(0, END)
# entry = CTkEntry(app)
# entry.grid(row=0, column=0 , sticky=NSEW)
# div = CTkButton(app , text = "Divide" , command= lambda : press("+"))
# div.grid(row=1, column=0, sticky=NSEW)
# eq = CTkButton(app , text = "Equal" , command = calculate)
# eq.grid(row=2, column=0, sticky=NSEW )
#
#
#
# app.mainloop()











