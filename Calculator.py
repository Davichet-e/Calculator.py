from math import cos, factorial, log, sin, sqrt, tan
from tkinter import Button, Entry, Frame, StringVar, Tk
from tkinter.constants import DISABLED, FLAT

root = Tk()

myFrame = Frame(root)

root.title("Calculator")

root.resizable(False, False)

myFrame.pack()

operation = ""

resetScreen = False

result = 0


#----Screen----#

numberScreen = StringVar()

screen = Entry(myFrame, textvariable=numberScreen, state="readonly",
                 readonlybackground="black", bd=20, relief=FLAT, fg='#9FEAF4')
screen.grid(row=1, column=1, columnspan=10, sticky='we')
screen.config(justify="right")
numberScreen.set("0")

#----Numbers Pressed----#


def numberPressed(num):

    global operation
    global resetScreen

    if numberScreen.get() == '0':
        if num != '.':
            numberScreen.set("")

    if resetScreen != False:

        numberScreen.set(num)
        resetScreen = False

    else:
        if num == '.':
            if numberScreen.get().count('.') == 0:
                numberScreen.set(numberScreen.get() + num)
        else:
            if num == '0':
                if numberScreen.get() != '0':
                    numberScreen.set(numberScreen.get() + num)
            else:
                numberScreen.set(numberScreen.get() + num)


#----funcSum----#
counter_sum = 0


def funcSum(num):

    global counter_sum
    global operation
    global result
    global resetScreen

    result += float(num)

    operation = "+"

    resetScreen = True

    counter_sum += 1

    numberScreen.set(result)


#----funcSubs----#
num1 = 0

counter_funcSubs = 0


def funcSubs(num):

    global operation
    global result
    global num1
    global counter_funcSubs
    global resetScreen

    if counter_funcSubs == 0:
        if numberScreen.get() == '0':
            numberScreen.set("-")
        else:
            num1 = float(num)
            result = num1

    else:
        if len(numberScreen.get()) == 0:
            result = ""
            counter_funcSubs = -1
        else:
            if counter_funcSubs == 1:

                result = num1-float(num)

            else:

                result -= float(num)

        numberScreen.set(result)

        result = numberScreen.get()
    if numberScreen.get() != '-':
        counter_funcSubs += 1

        operation = "-"

        resetScreen = True

#----funcFact----#


def funcFact(num):
    global operation
    global resetScreen

    if float(num) >= 0:
        result = factorial(float(num))
        numberScreen.set(result)
    else:
        numberScreen.set("SUBNORMAL")
    resetScreen = True


#----funcMult----#
counter_multi = 0


def funcMul(num):

    global operation
    global result
    global num1
    global counter_multi
    global resetScreen

    if counter_multi == 0:

        num1 = float(num)

        result = num1

    else:

        if counter_multi == 1:

            result = num1*float(num)

        else:

            result = float(result)*float(num)

        numberScreen.set(result)

        result = numberScreen.get()

    counter_multi += 1

    operation = "*"

    resetScreen = True

#----funcDivision----#


counter_divi = 0


def funcDiv(num):

    global operation
    global result
    global num1
    global counter_divi
    global resetScreen

    if counter_divi == 0:

        num1 = float(num)

        result = num1

    else:

        if counter_divi == 1:

            result = num1/int(num)

        else:

            result = float(result)/float(num)

        numberScreen.set(result)

        result = numberScreen.get()

    counter_divi += 1

    operation = "/"

    resetScreen = True
#----funcDivision----#


counter_remain = 0


def funcRemain(num):

    global operation
    global result
    global num1
    global counter_remain
    global resetScreen

    if counter_remain == 0:

        num1 = int(num)

        result = num1

    else:

        if counter_remain == 1:

            result = int(num1) % int(num)

        else:

            result = int(result) % int(num)

        numberScreen.set(result)

        result = numberScreen.get()

    counter_remain += 1

    operation = "%"

    resetScreen = True

#----funcSqrt----#


def funcSqrt(num):
    global operation
    global resetScreen

    if float(num) >= 0:
        result = sqrt(float(num))
        numberScreen.set(result)
    else:
        numberScreen.set(str(sqrt(abs(float(num)))) + "i")

    resetScreen = True

#----funcSqrt----#


def funcSquare(num):
    global operation
    global resetScreen

    result = float(num)**2
    numberScreen.set(result)

    resetScreen = True
#----Trigonometric Functions----#


def funcTrigono(num, func):
    global operation
    global resetScreen

    result = func(float(num))
    numberScreen.set(result)

    resetScreen = True

#----Results----#


def results():

    global result
    global operation
    global counter_funcSubs
    global counter_multi
    global counter_divi
    global counter_remain

    if operation == "+":

        numberScreen.set(float(result)+float(numberScreen.get()))

        result = 0

    elif operation == "-":

        numberScreen.set(float(result)-float(numberScreen.get()))
        result = 0
        counter_funcSubs = 0

    elif operation == "*":

        numberScreen.set(float(result)*float(numberScreen.get()))
        result = 0
        counter_multi = 0

    elif operation == "/":

        numberScreen.set(float(result)/float(numberScreen.get()))
        result = 0
        counter_divi = 0
    elif operation == "%":
        numberScreen.set(int(result) % int(numberScreen.get()))
        result = 0
        counter_remain = 0

#----Reset----#


def reset():
    global counter_divi
    global counter_funcSubs
    global counter_multi
    global counter_remain
    global counter_sum
    global result
    global num1

    result = 0
    num1 = 0
    counter_divi = 0
    counter_funcSubs = 0
    counter_multi = 0
    counter_remain = 0
    counter_sum = 0
    numberScreen.set("0")


#----Row0----#
KeyReset = Button(myFrame, text='AC',
                  command=lambda: reset(), bg='#252440', fg='white')
KeyReset.config(height=4, width=8)
KeyReset.grid(row=2, column=0, columnspan=3, ipadx=33)
KeySqrt = Button(myFrame, text='√n',   bg="grey",
                 fg='white', command=lambda: funcSqrt(numberScreen.get()))
KeySqrt.config(height=4, width=8)
KeySqrt.grid(row=2, column=3)
KeyFact = Button(myFrame, text="n!",   bg="grey",
                 fg='white', command=lambda: funcFact(numberScreen.get()))
KeyFact.config(height=4, width=8)
KeyFact.grid(row=2, column=4)
KeyRemain = Button(myFrame, text='%',   bg="grey",
                   fg='white', command=lambda: funcRemain(numberScreen.get()))
KeyRemain.config(height=4, width=8)
KeyRemain.grid(row=2, column=5)

#----Row1----#
Key7 = Button(myFrame, text='7', bg='#81BEF7',
              command=lambda: numberPressed('7'))
Key7.config(height=4, width=8)
Key7.grid(row=3, column=1)
Key8 = Button(myFrame, text='8', bg='#81BEF7',
              command=lambda: numberPressed('8'))
Key8.config(height=4, width=8)
Key8.grid(row=3, column=2)
Key9 = Button(myFrame, text='9', bg='#81BEF7',
              command=lambda: numberPressed('9'))
Key9.config(height=4, width=8)
Key9.grid(row=3, column=3)
KeyDiv = Button(myFrame, text='➗',   bg="grey",
                fg='white', command=lambda: funcDiv(numberScreen.get()))
KeyDiv.config(height=4, width=8)
KeyDiv.grid(row=3, column=4)
KeySquare = Button(myFrame, text='x^2', bg='grey', fg='white',
                   command=lambda: funcSquare(numberScreen.get()))
KeySquare.config(height=4, width=8)
KeySquare.grid(row=3, column=5)
KeyCos = Button(myFrame, text='cos(x)', bg="grey",
                fg='white', command=lambda: funcTrigono(numberScreen.get(), cos))
KeyCos.config(height=4, width=8)
KeyCos.grid(row=3, column=5)
#----Row2----#
Key4 = Button(myFrame, text='4', bg='#81BEF7',
              command=lambda: numberPressed('4'))
Key4.config(height=4, width=8)
Key4.grid(row=4, column=1)
Key5 = Button(myFrame, text='5', bg='#81BEF7',
              command=lambda: numberPressed('5'))
Key5.config(height=4, width=8)
Key5.grid(row=4, column=2)
Key6 = Button(myFrame, text='6', bg='#81BEF7',
              command=lambda: numberPressed('6'))
Key6.config(height=4, width=8)
Key6.grid(row=4, column=3)
KeyMult = Button(myFrame, text='✖', bg="grey",
                 fg='white', command=lambda: funcMul(numberScreen.get()))
KeyMult.config(height=4, width=8)
KeyMult.grid(row=4, column=4)
KeySin = Button(myFrame, text='sin(x)', bg="grey",
                fg='white', command=lambda: funcTrigono(numberScreen.get(), sin))
KeySin.config(height=4, width=8)
KeySin.grid(row=4, column=5)

#----Row3----#
Key1 = Button(myFrame, text='1', bg='#81BEF7',
              command=lambda: numberPressed('1'))
Key1.config(height=4, width=8)
Key1.grid(row=5, column=1)
Key2 = Button(myFrame, text='2', bg='#81BEF7',
              command=lambda: numberPressed('2'))
Key2.config(height=4, width=8)
Key2.grid(row=5, column=2)
Key3 = Button(myFrame, text='3', bg='#81BEF7',
              command=lambda: numberPressed('3'))
Key3.config(height=4, width=8)
Key3.grid(row=5, column=3)
KeyRest = Button(myFrame, text='➖', bg="grey",
                 fg='white', command=lambda: funcSubs(numberScreen.get()))
KeyRest.config(height=4, width=8)
KeyRest.grid(row=5, column=4)
KeyTan = Button(myFrame, text='tan(x)', bg="grey",
                fg='white', command=lambda: funcTrigono(numberScreen.get(), tan))
KeyTan.config(height=4, width=8)
KeyTan.grid(row=5, column=5)
#----Row4----#
Key0 = Button(myFrame, text='0', bg='#81BEF7',
              command=lambda: numberPressed('0'))
Key0.config(height=4, width=8)
Key0.grid(row=6, column=1)
KeyComma = Button(myFrame, text=',', bg="grey",
                  fg='white', command=lambda: numberPressed("."))
KeyComma.config(height=4, width=8)
KeyComma.grid(row=6, column=2)
KeyEqual = Button(myFrame, text='=', bg="grey",
                  fg='white', command=lambda: results())
KeyEqual.config(height=4, width=8)
KeyEqual.grid(row=6, column=3)
KeySum = Button(myFrame, text='➕', bg="grey",
                fg='white', command=lambda: funcSum(numberScreen.get()))
KeySum.config(height=4, width=8)
KeySum.grid(row=6, column=4)
KeyLog = Button(myFrame, text='ln(x)', bg="grey",
                fg='white', command=lambda: funcTrigono(numberScreen.get(), log))
KeyLog.config(height=4, width=8)
KeyLog.grid(row=6, column=5)


root.mainloop()
