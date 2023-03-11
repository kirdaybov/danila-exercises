from tkinter import *
import tkinter.messagebox
 
def calculate_tax():
    actual_cost = float(actual_cost_entry.get())
    assessed_value = actual_cost * 0.6
    property_tax = assessed_value / 100 * 0.75

    tkinter.messagebox.showinfo('Результат', 'Налог на акр равен: ' + str(property_tax))


main_window = Tk()
top_frame = Frame()
midle_frame = Frame()
bottom_frame = Frame()

actual_cost_lbl = Label(top_frame, text='Введите фактическую стоимость:')
actual_cost_entry = Entry(top_frame, width=10)

actual_cost_lbl.pack(side='left')
actual_cost_entry.pack(side='left')

button_calculate = Button(bottom_frame, text='Посчитать', command=calculate_tax)
quit_button = Button(bottom_frame,text='Выйти',command=main_window.destroy)

button_calculate.pack(side = 'left')
quit_button.pack(side = 'left')

top_frame.pack()
midle_frame.pack()
bottom_frame.pack()

main_window.mainloop()