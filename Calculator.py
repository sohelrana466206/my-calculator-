from tkinter import *
screen = Tk()
screen.title('Sohel Calculator')
screen.geometry('366x490')

def click(number):
    global operator
    operator += str(number)
    text.set(operator)

def clear():
    global operator
    operator = ''
    text.set(operator)

def equal():
    global operator
    result = eval(operator)
    operator = str(result)
    text.set(result)


text = StringVar()
operator = ''


entry1 = Entry(screen,bg='orange',font=('times',20,'italic bold'),bd='30',justify='right',text=text)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text='7',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(7))
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(8))
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(9))
btn9.grid(row=1,column=2)

btnadd = Button(screen,text='+',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click('+'))
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(4))
btn4.grid(row=2,column=0)

btn5 = Button(screen,text='5',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(5))
btn5.grid(row=2,column=1)

btn6 = Button(screen,text='6',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(6))
btn6.grid(row=2,column=2)

btnsub = Button(screen,text='-',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click('-'))
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text='1',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(1))
btn1.grid(row=3,column=0)

btn2 = Button(screen,text='2',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(2))
btn2.grid(row=3,column=1)

btn3 = Button(screen,text='3',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(3))
btn3.grid(row=3,column=2)

btnmul = Button(screen,text='*',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click('*'))
btnmul.grid(row=3,column=3)

btn0 = Button(screen,text='0',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(0))
btn0.grid(row=4,column=0)

btnclear = Button(screen,text='C',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=clear)
btnclear.grid(row=4,column=1)

btnequal = Button(screen,text='=',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=equal)
btnequal.grid(row=4,column=2)

btndiv = Button(screen,text='/',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click('/'))
btndiv.grid(row=4,column=3)



screen.mainloop()