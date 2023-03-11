from tkinter import *
import tkinter.messagebox

def calculate_Farengeit():
    celsius = float(celsius_entry.get())
    Farengeit = 9 /5 * celsius + 32
    tkinter.messagebox.showinfo('Результат', str(celsius) + ' градусов Цельсия равно = ' + str(Farengeit) + ' Фаренгейта')

main_window = Tk()
top_frame = Frame()
bottom_frame = Frame()

celsius_lbl = Label(top_frame, text='Введите гадусы Цельсия:')
celsius_entry = Entry(top_frame, width=10)

celsius_lbl.pack(side='left')
celsius_entry.pack(side='left')

button_calculate = Button(bottom_frame, text='Преобразовать', command=calculate_Farengeit)
quit_button = Button(bottom_frame,text='Выйти',command=main_window.destroy)

button_calculate.pack(side = 'left')
quit_button.pack(side = 'left')

top_frame.pack()
bottom_frame.pack()

main_window.mainloop()