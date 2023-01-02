import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.main_frame = MainWindow(self)
        self.install_frame = InstallWindow(self)
        self.confirm_uninstall = ConfirmUninstallWindow(self)


class InstallWindow(tk.Frame):
    name_field_default = 'Name'
    version_field_default = 'Version'
    path_field_default = 'Path'
    defaults = {
        'name_field_var':    name_field_default,
        'version_field_var': version_field_default,
        'path_field_var':    path_field_default
    }

    def __init__(self, master=None):
        super().__init__(master)

        # Cancel button (return to main screen)
        self.cancel_button = tk.Button(master=self, text='Cancel')
        self.cancel_button.pack(side=tk.BOTTOM)

        # Name field
        self.name_field_var = tk.StringVar(value=self.name_field_default)
        self.name_field = tk.Entry(master=self, textvariable=self.name_field_var)
        self.name_field.pack(side=tk.TOP)

        # Version field
        self.version_field_var = tk.StringVar(value=self.version_field_default)
        self.version_field = tk.Entry(master=self, textvariable=self.version_field_var)
        self.version_field.pack(side=tk.TOP)

        # Path Container
        self.path_container = tk.Frame(master=self)
        self.path_container.pack(side=tk.TOP)

        # Path field
        self.path_field_var = tk.StringVar(value=self.path_field_default)
        self.path_field = tk.Entry(master=self.path_container,
                                   textvariable=self.path_field_var,
                                   state=tk.DISABLED)
        self.path_field.pack(side=tk.LEFT)

        # Path search button
        self.path_search_button = tk.Button(master=self.path_container,
                                            text='Search...')
        self.path_search_button.pack(side=tk.RIGHT)

        # Scenario Container
        self.scenario_container = tk.Frame(master=self)
        self.scenario_container.pack(side=tk.BOTTOM)

        # Scenario check box
        self.scenario_var = tk.BooleanVar(master=self.scenario_container,
                                          value=False)

        self.scenario_checkbutton = tk.Checkbutton(master=self.scenario_container,
                                                   variable=self.scenario_var)
        self.scenario_checkbutton.pack(side=tk.LEFT)

        self.scenario_label = tk.Label(master=self.scenario_container,
                                       text='Install an ST Scenario')
        self.scenario_label.pack(side=tk.RIGHT)


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

        # Container for buttons
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

        # Quit Button
        self.quit_button = tk.Button(master=self.button_container, text='Quit',
                                     state=tk.NORMAL)
        self.quit_button.pack(side=tk.BOTTOM)

        # Tuple containing each button in the GUI
        self.buttons = (self.launch_button, self.install_button, self.uninstall_button, self.quit_button)
