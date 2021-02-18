import random
from tkinter import *
import time

winn = Tk()
winn.geometry("400x600")

#qiwi
win = 0
lose = 0
rie = 0
Mylist = ["камень","ножницы","бумага"]

bot_img1 = PhotoImage("bumaga1.png")
bot_img2 = PhotoImage("kamen1.png")
bot_img3 = PhotoImage("nozhnicy1.png")

def sup():
    global num
    num = int(ans1.get())

def end():
    label1.config(text=f"Вы выиграл {win} раз")
    lb.config(text=f"Вы проиграл {lose} раз")
    label3.config(text=f"Была ничя {rie} раз")
    label4.config(text = "END", font =("Helvetica", 20))

'''
def run():
    global rie, win, lose
    if num == 0:
        end()
    b = random.choice(Mylist)
    c = ans2.get()
    if b == Mylist[0] and c == Mylist[0]:
        rie = rie + 1
    elif b == Mylist[0] and c == Mylist[1]:
        lose = lose + 1
    elif b == Mylist[0] and c == Mylist[2]:
        win = win + 1
    elif b == Mylist[1] and c == Mylist[0]:
        win = win + 1
    elif b == Mylist[1] and c == Mylist[1]:
        rie = rie + 1
    elif b == Mylist[1] and c == Mylist[2]:
        lose = lose + 1
    elif b == Mylist[2] and c == Mylist[0]:
        lose = lose + 1
    elif b == Mylist[2] and c == Mylist[1]:
        win = win + 1
    elif b == Mylist[2] and c == Mylist[2]:
        rie = rie + 1
    elif c == 'q':
        end()
    lb_comp.config(text = f"компютер быврал {b}!")'''

def run1():
    global rie, win, lose
    b = random.choice(Mylist)
    c = "камень"
    if b == "камень":
        rie = rie + 1
        lb.config(image=bot_img2)
    elif b == "ножницы":
        win = win + 1
        lb.config(image=bot_img3)
    elif b == "бумага":
        lose = lose + 1
        lb.config(image=bot_img1)
    elif c == 'q':
        end()
    lb_comp.config(text=f"компютер быврал {b}!")


#bot_img1 = PhotoImage("bumaga1.png")
#bot_img2 = PhotoImage("kamen1.png")
#bot_img3 = PhotoImage("nozhnicy1.png")
#Mylist = ["камень","ножницы","бумага"]

def run2():
    global rie, win, lose
    b = random.choice(Mylist)
    c = "ножницы"
    if b == "камень":
        lose = lose + 1
        lb.config(image=bot_img2)
    elif b == "ножницы":
        rie = rie + 1
        lb.config(image=bot_img3)
    elif b == "бумага":
        win = win + 1
        lb.config(image=bot_img1)
    elif c == 'q':
        end()
    lb_comp.config(text = f"компютер быврал {b}!")
#Mylist = ["камень","ножницы","бумага"]

def run3():
    global rie, win, lose
    b = random.choice(Mylist)
    c = "бумага"
    if b == "камень":
        win = win + 1
        lb.config(image=bot_img2)
    elif b == "ножницы":
        lose = lose + 1
        lb.config(image=bot_img3)
    elif b == "бумага":
        rie = rie + 1
        lb.config(image=bot_img1)
    elif c == 'q':
        end()
    lb_comp.config(text = f"компютер быврал {b}!")
#Mylist = ["камень","ножницы","бумага"]



img1 = PhotoImage(file='kamen.png')
img2 = PhotoImage(file='nozhnicy.png')
img3 = PhotoImage(file='bumaga.png')
bot_img = PhotoImage(file='bot.png')

label1 = Label(winn,text ="Камень, ножницы или бумага", font =("Helvetica", 20))
label1.pack()
lb = Label(winn, text = "", font =("Helvetica", 12), image = bot_img)
lb.pack()
label2 = Label(winn, text = "сколько игр ты хочеш сыграть? (челое число)?", font =("Helvetica", 12))
#label2.pack()
btn1 = Button(winn, text = "Ввести!", font =("Helvetica", 12), command = sup)
#btn1.pack()
label3 = Label(winn, text="Что ты выбираеш:", font =("Helvetica", 12))
label4 = Label(winn, text="Камень, ножницы или бумага?", font =("Helvetica", 12))
label3.pack()
label4.pack()

btn2 = Button(winn, text = "камень", command = run1, font =("Helvetica", 12), image=img1)
btn2.place(x = 142, y = 290)
btn3 = Button(winn, text = "ножницы", command = run2, font =("Helvetica", 12), image=img2)
btn3.place(x = 20, y = 290)
btn4 = Button(winn, text = "бумага", command = run3, font =("Helvetica", 12), image=img3)
btn4.place(x = 263, y = 290)
lb_comp = Label(winn, text = " ", font =("Helvetica", 12))
lb_comp.place(x = 95, y = 458)
end_b = Button(winn, text = "Если хочиш закнчить - жми на меня", command = end, font =("Helvetica", 12))
end_b.place(x = 57, y = 480)


#lambda: run(str(ans1.get()))
winn.mainloop()