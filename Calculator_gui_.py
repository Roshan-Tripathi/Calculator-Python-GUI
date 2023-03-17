from tkinter import *
from tkinter import ttk
root=Tk()
root.config(background="black")
root.title("Roshan's  Calculator")
#variable
input_given=StringVar()
output=StringVar()
#empty string
value=""
#Number functions
def fun1():
    global value
    value = value + "1"
    input_given.set(value)
def fun2():
    global value
    value = value + "2"
    input_given.set(value)
def fun3():
    global value
    value = value + "3"
    input_given.set(value)
def fun4():
    global value
    value = value + "4"
    input_given.set(value)
def fun5():
    global value
    value = value + "5"
    input_given.set(value)
def fun6():
    global value
    value = value + "6"
    input_given.set(value)
def fun7():
    global value
    value = value + "7"
    input_given.set(value)
def fun8():
    global value
    value = value + "8"
    input_given.set(value)
def fun9():
    global value
    value = value + "9"
    input_given.set(value)
def fun0():
    global value
    value = value + "0"
    input_given.set(value)
def fun_clear():
    global value
    value=""
    input_given.set(value)
#symbol functions
def fun_plus():
    global value
    value = value + " + "
    input_given.set(value)
def fun_multi():
    global value
    value = value + " * "
    input_given.set(value)
def fun_divide():
    global value
    value = value + " / "
    input_given.set(value)
def fun_minus():
    global value
    value = value + " - "
    input_given.set(value)
def fun_dot():
    global value
    value = value + "."
    input_given.set(value)
#calculating operation
def output_value():
    global value
    output.set(eval(value))

#window size
root.geometry("948x568")
root.minsize(width=948,height=568)
root.maxsize(width=948,height=568)
#Frame in window
result=Frame(width=948,height=70,bg="blue",relief="sunken",bd=5)
result.pack(anchor="w")
num=Frame(width=948,height=350,bg="green",relief="solid",bd=5)
num.pack(anchor="w")
#creating number button
#column 0
seven=Button(num,text="7",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun7)
seven.grid(row=0,column=0)
four=Button(num,text="4",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun4)
four.grid(row=1,column=0)
one=Button(num,text="1",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun1)
one.grid(row=2,column=0)
zero=Button(num,text="0",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun0)
zero.grid(row=3,column=0)
#column 1
eight=Button(num,text="8",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun8)
eight.grid(row=0,column=1)
five=Button(num,text="5",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun5)
five.grid(row=1,column=1)
two=Button(num,text="2",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun2)
two.grid(row=2,column=1)
dot=Button(num,text=".",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun_dot)
dot.grid(row=3,column=1)
#column 2
nine=Button(num,text="9",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun9)
nine.grid(row=0,column=2)
six=Button(num,text="6",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun6)
six.grid(row=1,column=2)
three=Button(num,text="3",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun3)
three.grid(row=2,column=2)
divide=Button(num,text="/",font="bold 35",bg="orange",fg="red",width=9,height=2,command=fun_divide)
divide.grid(row=3,column=2)
#column 3
multiply=Button(num,text="X",font="bold 35",bg="orange",fg="red",width=9,height=2,command=fun_multi)
multiply.grid(row=0,column=3)
minus=Button(num,text="-",font="bold 35",bg="orange",fg="red",width=9,height=2,command=fun_minus)
minus.grid(row=1,column=3)
plus=Button(num,text="+",font="bold 35",bg="orange",fg="red",width=9,height=2,command=fun_plus)
plus.grid(row=2,column=3)
equal=Button(num,text="=",font="bold 35",bg="orange",fg="red",width=9,height=2,command=output_value)
equal.grid(row=3,column=3)

#add scroll bar
sb1_label=Label(result,text="Scroll bar",bg="yellow",fg="black",relief="solid",bd=3)
sb1_label.grid(row=2,sticky="w",padx=2,pady=3)
sb1=Scrollbar(result,orient="horizontal",bg="green",relief="solid",bd=3,width=17)
sb1.grid(row=2,sticky="w",padx=80,pady=2)

sb2=Scrollbar(result,orient="horizontal",bg="green",relief="solid",bd=3,width=17)
sb2.grid(row=2,sticky="w",padx=130,pady=2)
#type bar
type_space=Entry(result,width=37,bg="white",fg="black",font="bold 40",textvariable=input_given,xscrollcommand=sb1.set)
type_space.grid(row=0,column=0)
#clear button
clear=Button(result,text="CLEAR",font="bold 25",bg="orange",fg="Red",width=10,height=2,command=fun_clear)
clear.grid(row=1,column=0,sticky="e",padx=20,pady=5)
#Result space
result_space=Entry(result,width=31,bg="white",fg="black",font="bold 35",textvariable=output,xscrollcommand=sb2.set)
result_space.grid(row=1,column=0,sticky="w",padx=1)

sb2.config(command=result_space.xview)
sb1.config(command=type_space.xview)


root.mainloop()