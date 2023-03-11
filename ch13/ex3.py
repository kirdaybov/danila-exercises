from tkinter import *
import tkinter.messagebox

def calculate_consumption():
    miles = float(miles_entry.get())
    gallons = float(gallons_entry.get())
    result = miles / gallons
    tkinter.messagebox.showinfo('Результат', 'Показатель миль на галлоны: ' + str(result))


main_window = Tk()
top_frame = Frame()
midle_frame = Frame()
bottom_frame = Frame()

miles_lbl = Label(top_frame, text='Введите мили:')
miles_entry = Entry(top_frame, width=10)

miles_lbl.pack(side='left')
miles_entry.pack(side='left')

gallons_lbl = Label(midle_frame, text='Введите галлоны:')
gallons_entry = Entry(midle_frame, width=10)

gallons_lbl.pack(side='left')
gallons_entry.pack(side='left')

button_calculate = Button(bottom_frame, text='Посчитать', command=calculate_consumption)
quit_button = Button(bottom_frame,text='Выйти',command=main_window.destroy)

button_calculate.pack(side = 'left')
quit_button.pack(side = 'left')

top_frame.pack()
midle_frame.pack()
bottom_frame.pack()

main_window.mainloop()