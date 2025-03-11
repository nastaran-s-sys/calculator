import math

from customtkinter import *

from setting import *

from entry import *

from precent_btn import *
from CE_btn import *
from C_btn import *
from backspace import *

from x1_btn import *
from x2_btn import *
from x3_btn import *
from division import *

from btn_7  import *
from btn_8 import *
from btn_9  import *
from multiplication import *

from btn_4  import *
from btn_5 import *
from btn_6  import *
from minus import *

from btn_3  import *
from btn_2 import *
from btn_1 import *
from sum import *

from btn_x  import *
from btn_0 import *
from btn_dot import *
from equal import *

app = Window()
#####################################################row_0
###############################entry btn
entry = Entry(app)
entry.grid(row=0, column=0 , sticky=NSEW , columnspan=4 , padx=10, pady=10)
#####################################################row_1
###############################precent btn
def click_precent_btn():
    try:
        value = entry.get()
        number = float(value)
        number = number * (1/100)
        entry.delete(0, END)
        entry.insert(0, str(f"{value} *%  = {number}"))
    except:
        entry.delete(0, END)
precent_btn = PrecentBtn(app , command= click_precent_btn)
precent_btn .grid(row=1, column=0 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################CE btn
def click_CE_btn():
    entry.delete(0, END)
CE_btn = CEBtn(app , command= click_CE_btn)
CE_btn.grid(row=1, column=1 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################C btn
def click_C_btn():
    entry.delete(0, END)
C_btn = CBtn(app , command = click_C_btn)
C_btn.grid(row=1, column=2 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################backspace.
def backspace_btn():
    current_txt = entry.get()
    new_txt = current_txt[:-1]
    entry.delete(0, END)
    entry.insert(0, new_txt)
backspace= Backspace(app , text = "◄", command=backspace_btn)
backspace.grid(row=1, column=3 , sticky=NSEW, padx = 1.5 , pady = 2  )
#####################################################row_2
###############################btn_X
def click_x1():
    try:
        value = entry.get()
        number = float(value)
        number = (1/number)
        entry.delete(0, END)
        entry.insert(0, str(f"1/({value})  = {number}"))
    except:
        entry.delete(0, END)
    if value == "0":
        entry.insert(0, str("cannot divide by zero"))
x1_btn = X1(app , command= click_x1)
x1_btn.grid(row=2, column=0 , sticky=NSEW , padx = 1.5 , pady = 2 )
###############################btn_2
def click_x2():
    try:
        value = entry.get()
        number = float(value)
        number = number * number
        entry.delete(0, END)
        entry.insert(0, str(f"({value})²  = {number}"))
    except:
        entry.delete(0, END)
x2_btn= X2(app , command= click_x2)
x2_btn.grid(row=2, column=1 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################btn_3
def click_x3():
    try:
        value = entry.get()
        number = float(value)
        number = math.sqrt(number)
        entry.delete(0, END)
        entry.insert(0, str(f"√({value}) = {number}"))
    except:
        entry.delete(0, END)
x3_btn= X3(app , command= click_x3)
x3_btn.grid(row=2, column=2 , sticky=NSEW , padx = 1.5 , pady = 2)
################replace
def operator(new_operator):
    value = entry.get()
    operators = "+-*/"
    if not value :
        return
    for char in operators:
        if char in value:
            j = value.replace(char, new_operator)
            entry.delete(0, END)
            entry.insert(END , j)
            break
    if char not in value:
        entry.insert(END, new_operator)
###############################division
division= Division(app , command= lambda: operator("/"))
division.grid(row=2, column=3 , sticky=NSEW , padx = 1.5 , pady = 2)

#####################################################row_3
###############################btn_7
def btn_7_():
    entry.insert(END , 7)
btn_7 = Btn7(app , command= btn_7_)
btn_7.grid(row=3, column=0 , sticky=NSEW, padx = 1.5 , pady = 2 )
###############################btn_8
def btn_8_():
    entry.insert(END , 8)
btn_8= Btn8(app , command = btn_8_)
btn_8.grid(row=3, column=1 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################btn_9
def btn_9():
    entry.insert(END , 9)
btn_9= Btn9(app , command = btn_9)
btn_9.grid(row=3, column=2 , sticky=NSEW, padx = 1.5 , pady = 2 )
###############################multiplication

multiplication= Multiplication(app  , command= lambda: operator("*"))
multiplication.grid(row=3, column=3 , sticky=NSEW , padx = 1.5 , pady = 2)

#####################################################row_4
###############################btn_4
def btn_4_():
    entry.insert(END , 4)
btn_4 = Btn4(app , command= btn_4_ )
btn_4.grid(row=4, column=0 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################btn_5
def btn_5_():
    entry.insert(END , 5)
btn_5= Btn5(app , command= btn_5_ )
btn_5.grid(row=4, column=1 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################btn_6
def btn_6_():
    entry.insert(END , 6)
btn_6= Btn6(app , command= btn_6_ )
btn_6.grid(row=4, column=2 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################minus

minus= Minus(app , command= lambda: operator("-"))
minus.grid(row=4, column=3 , sticky=NSEW , padx = 1.5 , pady = 2)

#####################################################row_5
###############################btn_1
def btn_1_():
    entry.insert(END , 1)
btn_1 = Btn1(app , command= btn_1_)
btn_1.grid(row=5, column=0 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################btn_2
def btn_2_():
    entry.insert(END , 2)
btn_2= Btn2(app , command= btn_2_)
btn_2.grid(row=5, column=1 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################btn_3
def btn_3_():
    entry.insert(END , 3)
btn_3= Btn3(app , command = btn_3_)
btn_3.grid(row=5, column=2 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################sum
sum= Sum(app , command= lambda: operator("+"))
sum.grid(row=5, column=3 , sticky=NSEW , padx = 1.5 , pady = 2)

#####################################################row_6
###############################btn_x
# def X():
#     s = entry.get()
#     n = int(s)
#     j = -n
#     entry.delete(0,END)
#     entry.insert(END, j)
# i have an problem with this btn
btn_x = BtnX(app
             # , command= X
             )
btn_x.grid(row=6, column=0 , sticky=NSEW, padx = 1.5 , pady = 2 )
###############################btn_0
def btn_0_():
    entry.insert(END , 0)
btn_0= Btn0(app , command= btn_0_)
btn_0.grid(row=6, column=1 , sticky=NSEW, padx = 1.5 , pady = 2 )
###############################btn_dot
def dot():
    value = entry.get()
    if value == "":
        return
    if "." not in value:
        entry.insert(END, str("."))
btn_dot= Dot(app , command= dot )
btn_dot.grid(row=6, column=2 , sticky=NSEW , padx = 1.5 , pady = 2)
###############################keyboard
def key_handler(event):
    allowed_keys = "0123456789"
    special_keys = ["Return", "BackSpace"]
    if event.char not in allowed_keys and event.keysym not in special_keys:
        return "break"
entry.bind("<Key>", key_handler)
#################################equel
def equel():
    try:
        calculte = entry.get()
        result = eval(calculte)
        s = entry.get()
        if division:
            j = s.replace('/', ' ÷ ')
            entry.delete(0, END)
            entry.insert(0, f"{j} =  {result}")
        elif multiplication:
            j = s.replace('*', ' ⨉× ')
            entry.delete(0, END)
            entry.insert(0, f"{j} =  {result}")

    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0 , "Division by zero")
    except:
        entry.delete(0, END)

equal= Equal(app , command= equel)
equal.grid(row=6, column=3 , sticky=NSEW , padx = 1.5 , pady = 2)



if __name__ == '__main__':
    app.mainloop()