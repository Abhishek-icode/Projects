from tkinter import *

def click(event):
    global cvalue
    text = event.widget.cget("text")
    if text == "=":
        if cvalue.get().isdigit():
            value = int(cvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
        cvalue.set(value)
        screen.update()
    elif text == "X":
        cvalue.set("")
        screen.update()
    else:
        cvalue.set(cvalue.get() + text)
        screen.update()
root =Tk()
root.geometry("1366x768")
root.title("Calculator")
# root.wm_iconbitmap("3440925-business-calculator-ecommerce-finance-marketing-math-office_107525 (1).ico")

cvalue = StringVar()
cvalue.set("")

screen = Entry(root, text=cvalue, font=("times", 99),  bg="navy", fg="white")
screen.pack(fill=X)

f1 = Frame(root)
b1 = Button(f1, text="1", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b2 = Button(f1, text="2", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b2.pack(side=LEFT)
b2.bind("<Button-1>", click)
b3 = Button(f1, text="3", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b3.pack(side=LEFT)
b3.bind("<Button-1>", click)
bdiv = Button(f1, text="/", bg="navy", fg="white", font=("times", 33), padx=147, pady=12, command=click)
bdiv.pack(side=LEFT)
bdiv.bind("<Button-1>", click)
f1.pack(fill=X)

f1 = Frame(root)
b1 = Button(f1, text="4", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b2 = Button(f1, text="5", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b2.pack(side=LEFT)
b2.bind("<Button-1>", click)
b3 = Button(f1, text="6", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b3.pack(side=LEFT)
b3.bind("<Button-1>", click)
bdiv = Button(f1, text="*", bg="navy", fg="white", font=("times", 33), padx=143, pady=12, command=click)
bdiv.pack(side=LEFT)
bdiv.bind("<Button-1>", click)
f1.pack(fill=X)

f1 = Frame(root)
b1 = Button(f1, text="7", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b2 = Button(f1, text="8", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b2.pack(side=LEFT)
b2.bind("<Button-1>", click)
b3 = Button(f1, text="9", bg="dark green", fg="white", font=("times", 33), padx=143, pady=12, command=click)
b3.pack(side=LEFT)
b3.bind("<Button-1>", click)
bdiv = Button(f1, text="-", bg="navy", fg="white", font=("times", 33), padx=147, pady=12, command=click)
bdiv.pack(side=LEFT)
bdiv.bind("<Button-1>", click)
f1.pack(fill=X)

f1 = Frame(root)
b1 = Button(f1, text=".", bg="dark green", fg="white", font=("times", 33), padx=149, pady=12, command=click)
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b2 = Button(f1, text="0", bg="dark green", fg="white", font=("times", 33), padx=142, pady=12, command=click)
b2.pack(side=LEFT)
b2.bind("<Button-1>", click)
b3 = Button(f1, text="=", bg="orangered3", fg="white", font=("times", 33), padx=142, pady=12, command=click)
b3.pack(side=LEFT)
b3.bind("<Button-1>", click)
bdiv = Button(f1, text="+", bg="navy", fg="white", font=("times", 33), padx=145, pady=12, command=click )
bdiv.pack(side=LEFT)
bdiv.bind("<Button-1>", click)
f1.pack(fill=X)

f1 = Frame(root)
b0 = Button(f1, text="X", bg="dark red", fg="white", font=("lucida", 33), width=99, pady=12, command=click )
b0.pack(side=LEFT)
b0.bind("<Button-1>", click)
f1.pack(fill=X)

root.mainloop()