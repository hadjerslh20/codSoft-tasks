from tkinter import *
import math
windowClac=Tk()
windowClac.geometry('240x387+600+200')
windowClac.resizable(FALSE,FALSE)
windowClac.title('Calculator')
windowClac.config(background='#e3e3e3')
screen_result= Entry(windowClac,bd=1,width=40,bg='#455d7a',font=("arial",40),fg='white',insertbackground="white")
def click(num):
    screen_result.insert(32 ,num)
def clear():
    screen_result.delete(0, END) 
def evaluate():
    try:
        expression = screen_result.get()
        expression = expression.replace('÷', '/')  # Replace ÷ with /
        if '√' in expression:  # Check for square root
            while '√' in expression:
                start = expression.index('√')  # Find the index of '√'
                end = start + 1
                while end < len(expression) and (expression[end].isdigit() or expression[end] == '.'):
                    end += 1
                num = float(expression[start+1:end])  # Extract the number after √
                sqrt_result = math.sqrt(num)  # Compute square root
                expression = expression[:start] + str(sqrt_result) + expression[end:]  # Replace √number with result
        result = eval(expression)  # Evaluate the modified expression
        screen_result.delete(0, END)
        screen_result.insert(END, result)  # Display the result
    except Exception as e:
        screen_result.delete(0, END)
        screen_result.insert(END, "Error")  # Display error message
screen_result.pack()
btn1=Button(windowClac,text='C',font='Arial 19 bold',bg='#f95959',bd=1,padx=10,pady=5,fg='white',command = lambda :clear())
btn1.place(x=0,y=65)
btn2=Button(windowClac,text='x²',font='Arial 19 bold',bg='#233142',bd=1,padx=10,pady=5,fg='white',command = lambda :click('**'))
btn2.place(x=60,y=65)
btn3=Button(windowClac,text='√',font='Arial 19 bold',bg='#233142',bd=1,padx=10,pady=5,fg='white',command = lambda :click('√'))
btn3.place(x=124,y=65)
btn4=Button(windowClac,text='+',font='Arial 19 bold',bg='#233142',bd=1,padx=10,pady=5,fg='white',command = lambda :click('+'))
btn4.place(x=180,y=65)
btn5=Button(windowClac,text='÷',font='Arial 19 bold',bg='#233142',bd=1,padx=13,pady=5,fg='white',command = lambda :click('÷'))
btn5.place(x=180,y=130)
btn6=Button(windowClac,text='7',font='Arial 19 bold',bg='#233142',bd=1,padx=11,pady=5,fg='white',command = lambda :click(7))
btn6.place(x=0,y=130)
btn7=Button(windowClac,text='8',font='Arial 19 bold',bg='#233142',bd=1,padx=13,pady=5,fg='white',command = lambda :click(8))
btn7.place(x=60,y=130)
btn8=Button(windowClac,text='9',font='Arial 19 bold',bg='#233142',bd=1,padx=11,pady=5,fg='white',command = lambda :click(9))
btn8.place(x=122,y=130)
btn9=Button(windowClac,text='*',font='Arial 19 bold',bg='#233142',bd=1,padx=14,pady=5,fg='white',command = lambda :click('*'))
btn9.place(x=180,y=195)
btn10=Button(windowClac,text='4',font='Arial 19 bold',bg='#233142',bd=1,padx=11,pady=5,fg='white',command = lambda :click(4))
btn10.place(x=0,y=195)
btn11=Button(windowClac,text='5',font='Arial 19 bold',bg='#233142',bd=1,padx=13,pady=5,fg='white',command = lambda :click(5))
btn11.place(x=60,y=195)
btn12=Button(windowClac,text='6',font='Arial 19 bold',bg='#233142',bd=1,padx=11,pady=5,fg='white',command = lambda :click(6))
btn12.place(x=122,y=195)
btn13=Button(windowClac,text='-',font='Arial 19 bold',bg='#233142',bd=1,padx=14,pady=5,fg='white',command = lambda :click('-'))
btn13.place(x=180,y=260)
btn14=Button(windowClac,text='1',font='Arial 19 bold',bg='#233142',bd=1,padx=11,pady=5,fg='white',command = lambda :click(1))
btn14.place(x=0,y=260)
btn15=Button(windowClac,text='2',font='Arial 19 bold',bg='#233142',bd=1,padx=13,pady=5,fg='white',command = lambda :click(2))
btn15.place(x=60,y=260)
btn16=Button(windowClac,text='3',font='Arial 19 bold',bg='#233142',bd=1,padx=11,pady=5,fg='white',command = lambda :click(3))
btn16.place(x=122,y=260)
btn17=Button(windowClac,text='0',font='Arial 19 bold',bg='#233142',bd=1,padx=43,pady=5,fg='white',command = lambda :click(0))
btn17.place(x=0,y=325)
btn17=Button(windowClac,text='=',font='Arial 19 bold',bg='#118df0',bd=1,padx=38,pady=5,fg='white',command=evaluate)
btn17.place(x=125,y=325)
windowClac.mainloop()
