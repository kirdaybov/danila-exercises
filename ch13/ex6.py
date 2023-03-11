from tkinter import *
import tkinter.messagebox

def calc_costs():
    total = 0
    if cb_var1.get() == 1:
        total += 500
    if cb_var2.get() == 1:
        total += 300
    if cb_var3.get() == 1:
        total += 700
    if cb_var4.get() == 1:
        total += 1000
    if cb_var5.get() == 1:
        total += 800
    if cb_var6.get() == 1:
        total += 1300
    if cb_var7.get() == 1:
        total += 1300    
    tkinter.messagebox.showinfo('Результат', 'Ваши затраты равны: ' + str(total))

main_window = Tk()

top_frame = Frame(main_window)
bottom_frame = Frame(main_window)

cb_var1 = IntVar()
cb_var2 = IntVar()
cb_var3 = IntVar()
cb_var4 = IntVar()
cb_var5 = IntVar()
cb_var6 = IntVar()
cb_var7 = IntVar()

cb_var1.set(0)
cb_var2.set(0)
cb_var3.set(0)
cb_var4.set(0)
cb_var5.set(0)
cb_var6.set(0)
cb_var7.set(0)

cb1 = Checkbutton(top_frame, text='Замена масла - 500 руб.', variable=cb_var1)
cb2 = Checkbutton(top_frame, text='Смазочные работы - 300 руб.', variable=cb_var2)
cb3 = Checkbutton(top_frame, text='Промывка радиатора - 700 руб.', variable=cb_var3)
cb4 = Checkbutton(top_frame, text='Замена жидкости в трансмисии - 1000 руб.', variable=cb_var4)
cb5 = Checkbutton(top_frame, text='Осмотр - 800 руб.', variable=cb_var5)
cb6 = Checkbutton(top_frame, text='Замена глушителя выхлопа - 1300 руб.', variable=cb_var6)
cb7 = Checkbutton(top_frame, text='Перестановка шин - 1300 руб.', variable=cb_var7)

cb1.pack()
cb2.pack()
cb3.pack()
cb4.pack()
cb5.pack()
cb6.pack()
cb7.pack()

Show_costs_button = Button(bottom_frame, text='Показать затраты', command= calc_costs)
quit_batton = Button(bottom_frame,text='Выйти',command=main_window.destroy)

Show_costs_button.pack(side='left')
quit_batton.pack(side='left')

top_frame.pack()
bottom_frame.pack()

main_window.mainloop()
