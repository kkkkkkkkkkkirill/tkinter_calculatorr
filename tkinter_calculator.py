from tkinter import *
from tkinter.ttk import *
from math import sqrt


def add_display_1():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 1)


def add_display_2():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 2)


def add_display_3():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 3)


def add_display_4():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 4)


def add_display_5():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 5)


def add_display_6():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 6)


def add_display_7():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 7)


def add_display_8():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 8)


def add_display_9():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 9)


def add_display_0():
    if entry_display.get() == "0":
        entry_display.delete(0, END)
    entry_display.insert(END, 0)


def clear_display():
    entry_display.delete(0, END)
    entry_display.insert(END, 0)


def display_point():
    if entry_display.get().find(".") == -1:
        entry_display.insert(END, ".")


def display_sign_plus():
    if entry_display.get()[len(entry_display.get()) - 1] in f"+-/*%{chr(177)}{chr(8730)}":
        entry_display.delete(len(entry_display.get()) - 1)
    entry_display.insert(END, "+")


def display_sign_minus():
    if entry_display.get()[len(entry_display.get()) - 1] in f"+-/*%{chr(177)}{chr(8730)}":
        entry_display.delete(len(entry_display.get()) - 1)
    entry_display.insert(END, "-")


def display_sign_divide():
    if entry_display.get()[len(entry_display.get()) - 1] in f"+-/*%{chr(177)}{chr(8730)}":
        entry_display.delete(len(entry_display.get()) - 1)
    entry_display.insert(END, "/")


# def display_sign_percent():
#     if entry_display.get()[-1] in "+-/*":
#         entry_display.delete(len(entry_display.get())-1)
#     if entry_display.get().find("/0") != entry_display.get().find("/0."):
#         entry_display.delete(0, END)
#         entry_display.insert(END, "Cannot division by zero")
#     else:
#         answer_percent = eval(entry_display.get())/100
#         entry_display.delete(0, END)
#         entry_display.insert(END, answer_percent)


def display_sign_percent():
    display_count_equal()
    if not entry_display.get().replace(" ", "").isalpha():
        answer_percent = eval(entry_display.get())/100
        entry_display.delete(0, END)
        entry_display.insert(END, answer_percent)


def display_sign_multiply():
    if entry_display.get()[len(entry_display.get()) - 1] in f"+-/*%{chr(177)}{chr(8730)}":
        entry_display.delete(len(entry_display.get()) - 1)
    entry_display.insert(END, "*")


def display_sign_plus_minus():
    if entry_display.get()[-1] in "+-/*":
        entry_display.delete(len(entry_display.get())-1)
    if entry_display.get().find("/0") != entry_display.get().find("/0."):
        entry_display.delete(0, END)
        entry_display.insert(END, "Cannot division by zero")
    else:
        answer_plus_minus = -eval(entry_display.get())
        entry_display.delete(0, END)
        entry_display.insert(END, answer_plus_minus)


def display_sign_sqrt():
    if entry_display.get()[-1] in "+-/*":
        entry_display.delete(len(entry_display.get())-1)
    if entry_display.get().find("/0") != entry_display.get().find("/0."):
        entry_display.delete(0, END)
        entry_display.insert(END, "Cannot division by zero")
    elif eval(entry_display.get()) >= 0:
        answer_sqrt = sqrt(eval(entry_display.get()))
        entry_display.delete(0, END)
        entry_display.insert(END, answer_sqrt)
    else:
        entry_display.delete(0, END)
        entry_display.insert(END, "Invalid input")


def display_count_equal():
    if entry_display.get()[-1] in f"+-/*":
        entry_display.delete(len(entry_display.get())-1)
    if entry_display.get().find("/0") != entry_display.get().find("/0."):
        entry_display.delete(0, END)
        entry_display.insert(END, "Cannot division by zero")
    elif entry_display.get():
        answer = eval(entry_display.get())
        entry_display.delete(0, END)
        entry_display.insert(END, answer)


def display_one_division():
    if entry_display.get():
        answer_one_division = 1/eval(entry_display.get())
        entry_display.delete(0, END)
        entry_display.insert(END, answer_one_division)


root = Tk()
root.title("Calculator")
num = StringVar()
num.set(0)
entry_display = Entry(textvariable=num, justify=RIGHT)
entry_display.grid(column=0, row=0, columnspan=5, sticky=NSEW)
Button(root, text="MC").grid(column=0, row=1)
Button(root, text="MR").grid(column=1, row=1)
Button(root, text="MS").grid(column=2, row=1)
Button(root, text="M+").grid(column=3, row=1)
Button(root, text="M-").grid(column=4, row=1)

Button(root, text="<--").grid(column=0, row=2)
Button(root, text="CE").grid(column=1, row=2)
Button(root, text="C", command=clear_display).grid(column=2, row=2)
Button(root, text=chr(177), command=display_sign_plus_minus).grid(column=3, row=2)
Button(root, text=chr(8730), command=display_sign_sqrt).grid(column=4, row=2)

Button(root, text=7, command=add_display_7).grid(column=0, row=3)
Button(root, text=8, command=add_display_8).grid(column=1, row=3)
Button(root, text=9, command=add_display_9).grid(column=2, row=3)
Button(root, text="/", command=display_sign_divide).grid(column=3, row=3)
Button(root, text="%", command=display_sign_percent).grid(column=4, row=3)

Button(root, text=4, command=add_display_4).grid(column=0, row=4)
Button(root, text=5, command=add_display_5).grid(column=1, row=4)
Button(root, text=6, command=add_display_6).grid(column=2, row=4)
Button(root, text="*", command=display_sign_multiply).grid(column=3, row=4)
Button(root, text="1/x", command=display_one_division).grid(column=4, row=4)

Button(root, text=1, command=add_display_1).grid(column=0, row=5)
Button(root, text=2, command=add_display_2).grid(column=1, row=5)
Button(root, text=3, command=add_display_3).grid(column=2, row=5)
Button(root, text="-", command=display_sign_minus).grid(column=3, row=5)
Button(root, text="=", command=display_count_equal).grid(column=4, row=5, rowspan=2, sticky=NSEW)

Button(root, text=0, command=add_display_0).grid(column=0, row=6, columnspan=2, sticky=NSEW)
Button(root, text=".", command=display_point).grid(column=2, row=6)
Button(root, text="+", command=display_sign_plus).grid(column=3, row=6)

root.mainloop()
