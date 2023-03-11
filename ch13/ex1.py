from tkinter import *

def show_info():
    info_lbl.set('Мой адресс и прочая инфа')
    
main_window = Tk()
top_frame = Frame()
bottom_frame = Frame()

info_lbl = StringVar()
lbl = Label(top_frame, textvariable=info_lbl)
lbl.pack()

button_info = Button(bottom_frame, text='Показать инфо', command=show_info)
quit_button = Button(bottom_frame,text='Выйти',command=main_window.destroy)

button_info.pack(side = 'left')
quit_button.pack(side = 'left')

top_frame.pack()
bottom_frame.pack()

main_window.mainloop()