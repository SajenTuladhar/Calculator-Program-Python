from tkinter import *

def button_pressed(num):
    global equation_text

    equation_text =  equation_text +str(num)
    equation_label.set(equation_text) # text displayed on label in gui 

def equals():
    global equation_text
    try:
        total= str(eval(equation_text)) # eval takes string as input and excute it as integer
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set('Arithmetic error')
        equation_text=""

    except SyntaxError:
        equation_label.set('Syntax error')
        equation_text=""


def clear():
    global equation_text
    equation_label.set("")
    equation_text=""

window=Tk()
window.title('Calculator')
window.geometry('400x600')          

equation_text=""

equation_label= StringVar()

label= Label(window, textvariable=equation_label,font=('Arial',20),bg='white',width=30,height=2) # any change made to equation label will be reflected in label text
label.pack()

frame= Frame(window)
frame.pack()


button7= Button(frame,text=7,height=4,width=8,font=35,command=lambda:button_pressed(7))
button7.grid(row=0,column=0)

button8= Button(frame,text=8,height=4,width=8,font=35,command=lambda:button_pressed(8))
button8.grid(row=0,column=1)

button9= Button(frame,text=9,height=4,width=8,font=35,command=lambda:button_pressed(9))
button9.grid(row=0,column=2)

button4= Button(frame,text=4,height=4,width=8,font=35,command=lambda:button_pressed(4))
button4.grid(row=1,column=0)

button5= Button(frame,text=5,height=4,width=8,font=35,command=lambda:button_pressed(5))
button5.grid(row=1,column=1)

button6= Button(frame,text=6,height=4,width=8,font=35,command=lambda:button_pressed(6))
button6.grid(row=1,column=2)

button1= Button(frame,text=1,height=4,width=8,font=35,command=lambda:button_pressed(1))
button1.grid(row=2,column=0)

button2= Button(frame,text=2,height=4,width=8,font=35,command=lambda:button_pressed(2))
button2.grid(row=2,column=1)

button3= Button(frame,text=3,height=4,width=8,font=35,command=lambda:button_pressed(3))
button3.grid(row=2,column=2)

button0= Button(frame,text=0,height=4,width=8,font=35,command=lambda:button_pressed(0))
button0.grid(row=3,column=0)

Dec_point_button= Button(frame,text='.',height=4,width=8,font=35,command=lambda:button_pressed('.'))
Dec_point_button.grid(row=3,column=1)

equals_button= Button(frame,text='=',height=4,width=8,font=35,command=equals)
equals_button.grid(row=3,column=2)

add_button= Button(frame,text='+',height=4,width=8,font=35,command=lambda:button_pressed('+'))
add_button.grid(row=0,column=4)

subtract_button= Button(frame,text='-',height=4,width=8,font=35,command=lambda:button_pressed('-'))
subtract_button.grid(row=1,column=4)

multiply_button= Button(frame,text='x',height=4,width=8,font=35,command=lambda:button_pressed('x'))
multiply_button.grid(row=2,column=4)

divide_button= Button(frame,text='/',height=4,width=8,font=35,command=lambda:button_pressed('/'))
divide_button.grid(row=3,column=4)

Clear_button= Button(window,text='Clear',height=4,width=20,font=35,command=clear)
Clear_button.pack()
    
window.mainloop()       