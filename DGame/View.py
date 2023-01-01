import tkinter as tk

import Controller


class MainWindow(tk.Frame):
    def __init__(self, controller: Controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.pack()

        self.game_list_var = self.controller.get_game_names()
        self.game_list = tk.Listbox(master=self, listvariable=self.game_list_var)

        # self.entrythingy = tk.Entry()
        # self.entrythingy.pack()

        # # Create the application variable.
        # self.contents = tk.StringVar()
        # # Set it to some value.
        # self.contents.set("this is a variable")
        # # Tell the entry widget to watch this variable.
        # self.entrythingy["textvariable"] = self.contents

        # # Define a callback for when the user hits return.
        # # It prints the current value of the variable.
        # self.entrythingy.bind('<Key-Return>', self.print_contents)

