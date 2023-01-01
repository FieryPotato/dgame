import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.main_frame = MainWindow(self)
        self.add_frame = AddGameWindow(self)
        self.confirm_uninstall = ConfirmUninstallWindow(self)


class AddGameWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.cancel_button = tk.Button(master=self, text='Cancel')
        self.cancel_button.pack(side=tk.BOTTOM)


class ConfirmUninstallWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.cancel_button = tk.Button(master=self, text='Cancel')
        self.cancel_button.pack(side=tk.BOTTOM)


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Games list
        self.game_list_var = tk.Variable()
        self.game_list = tk.Listbox(master=self,
                                    listvariable=self.game_list_var,
                                    height=16)
        self.game_list.pack(side=tk.LEFT)

        self.button_container = tk.Frame(master=self)
        self.button_container.pack(side=tk.RIGHT)

        # Launch Game Button
        self.launch_button = tk.Button(master=self.button_container, text='Launch',
                                       state=tk.DISABLED)
        self.launch_button.pack(side=tk.TOP)

        # Install Game Button
        self.install_button = tk.Button(master=self.button_container, text='Install',
                                        state=tk.NORMAL)
        self.install_button.pack(side=tk.TOP)

        # Uninstall Game Button
        self.uninstall_button = tk.Button(master=self.button_container, text='Uninstall',
                                          state=tk.DISABLED)
        self.uninstall_button.pack(side=tk.TOP)

        # Tuple containing each button in the GUI
        self.buttons = (self.launch_button, self.install_button)
