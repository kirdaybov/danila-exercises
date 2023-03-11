from tkinter import *
import tkinter.messagebox

def calculate_cost():
    total = 0
    rate = radio_var.get()
    minut = int(minut_entry.get())
    if rate == 1:
        total = minut * 10
    elif rate == 2:
        total = minut * 12
    else:
        total = minut * 5
    tkinter.messagebox.showinfo('Результат', 'Стоимость вызова: ' + str(total))

main_window = Tk()
top_frame = Frame()
midle_frame = Frame()
bottom_frame = Frame()

radio_var = IntVar()
radio_var.set(1)

rb1 = Radiobutton(midle_frame, text='Дневное время (с 6:00 до 17:59)',variable=radio_var, value=1)
rb2 = Radiobutton(midle_frame, text='Вечернее время (с 18:00 до 23:59)',variable=radio_var, value=2)
rb3 = Radiobutton(midle_frame, text='Непиковый период (с полуночи до 5:59)',variable=radio_var, value=3)

rb1.pack()
rb2.pack()
rb3.pack()

minut_lbl = Label(top_frame, text='Введите продолжительность звонка в минутах: ')
minut_entry = Entry(top_frame, width=10)

minut_lbl.pack(side='left')
minut_entry.pack(side='left')

button_calculate = Button(bottom_frame, text='Посчитать', command=calculate_cost)
quit_button = Button(bottom_frame,text='Выйти',command=main_window.destroy)

button_calculate.pack(side = 'left')
quit_button.pack(side = 'left')

top_frame.pack()
midle_frame.pack()
bottom_frame.pack()

main_window.mainloop()