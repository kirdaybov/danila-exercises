import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text = 'Привет, мир',borderwidth=3,relief='ridge')

        self.label.pack(padx=10,pady=20)

        tkinter.mainloop()

my_gui = MyGui()