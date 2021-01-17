from tkinter import *
from tkinter import messagebox
import csv

dict_riddles = {}
status = []

with open('list_riddles.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    for s in reader:
        dict_riddles[s[0]] = s[1]


def generator_riddle(dict_riddles):
    global status
    for k, v in dict_riddles.items():
        if k not in status:
            return [k, v]


root = Tk()
root.title('Victorina')
root.geometry('400x250')

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))


def que_one(dict_riddles):
    riddles_response = generator_riddle(dict_riddles)

    counter = f'Разгадано: {len(status)} из {len(dict_riddles)}.'

    title = Label(root, text='Загадки для детей', font="Arial 16 bold", foreground="#191970")
    question = Label(root, text=riddles_response[0], wraplength=300, justify=CENTER, font="Arial 14",
                     foreground="#0000FF")
    answer = Entry()
    btn1 = Button(root, text='Ответить', command=lambda: game('Ответить'))
    btn2 = Button(root, text='Показать ответ', command=lambda: game('Показать ответ'))
    count = Label(root, text=counter)

    title.grid(row=1, padx=70)
    question.grid(row=2, padx=70)
    answer.grid(row=3)
    btn1.grid(row=4)
    btn2.grid(row=5)
    count.grid(row=6)

    def game(value):
        global status
        if answer.get().lower() == riddles_response[1].lower():
            status.append(riddles_response[0])
            question.destroy()
            que_one(dict_riddles)
        elif value == 'Показать ответ':
            messagebox.showinfo('Правильный ответ', f'{riddles_response[1]}')

        else:
            messagebox.showerror('Неверно', 'Попробуй еще раз!')


que_one(dict_riddles)

root.mainloop()
