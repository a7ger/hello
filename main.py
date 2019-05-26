#!/usr/bin/env python3

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_button = tk.Button(self)
        self.hello_button['text'] = 'click me to print "hello world"'
        self.hello_button['command'] = self.button_clicked
        self.hello_button.pack(side='top')

        self.quit_button = tk.Button(self, text='quit', command=self.master.destroy)
        self.quit_button.pack(side='bottom')

    def button_clicked(self):
        print('hello world')

app = App(master = tk.Tk())
app.mainloop()
