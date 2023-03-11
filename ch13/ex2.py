from tkinter import *

def show_sinister():
    info_lbl.set('левый')
    
def show_dexter():
    info_lbl.set('правый')

def show_medium():
    info_lbl.set('центральный')

main_window = Tk()
top_frame = Frame()
bottom_frame = Frame()

info_lbl = StringVar()
lbl = Label(top_frame, textvariable=info_lbl)
lbl.pack()

button_sinister = Button(bottom_frame, text='sinister', command=show_sinister)
button_dexter = Button(bottom_frame,text='dexter',command=show_dexter)
button_medium = Button(bottom_frame,text='medium',command=show_medium)

button_sinister.pack(side = 'left')
button_dexter.pack(side = 'left')
button_medium.pack(side = 'left')

top_frame.pack()
bottom_frame.pack()

main_window.mainloop()