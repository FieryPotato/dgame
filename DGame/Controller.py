import tkinter as tk
from tkinter import filedialog as fd

from Model import Model
from View import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

        self.initialize_frames()
        self.installed_games: list[str] = self.view.main_frame.game_list_var.get()
        self.view.main_frame.pack()

    def main_window(self) -> tk.Tk:
        self.view.title('DGame')
        return self.view

    def initialize_frames(self) -> None:
        # Initialize Main Frame
        # Initialize Main Frame Games List
        self.view.main_frame.game_list_var.set(self.model.read_game_names())
        self.view.main_frame.game_list.bind('<<ListboxSelect>>', self.switch_buttons_on)

        # Initialize Main Frame Launch button
        self.view.main_frame.launch_button.configure(command=self.launch_callback)

        # Initialize Main Frame Install button
        self.view.main_frame.install_button.configure(command=self.surface_installer)

        # Initialize Main Frame Uninstall button
        self.view.main_frame.uninstall_button.configure(command=self.surface_uninstall_confirm)

        # Initialize Main Frame Quit button
        self.view.main_frame.quit_button.configure(command=self.quit)

        # Initialize Install Frame
        # Initialize Path Search Button
        self.view.install_frame.path_search_button.configure(command=self.get_path)

        # Initialize Checkbox
        self.view.install_frame.scenario_label.bind('<Button-1>', self.toggle_scenario_checkbutton)
        self.view.install_frame.scenario_checkbutton.configure(command=self.toggle_install_fields)

        # Initialize Install Cancel Button
        self.view.install_frame.cancel_button.configure(command=self.surface_main)

        # Initialize Confirm Uninstall Frame
        # Initialize Cancel Button
        self.view.confirm_uninstall.cancel_button.configure(command=self.surface_main)

    def switch_buttons_on(self, *_) -> None:
        if self.model.database_is_empty(self.installed_games):
            return
        for button in self.view.main_frame.buttons:
            button['state'] = tk.NORMAL

    def launch_callback(self) -> None:
        if self.model.database_is_empty(self.installed_games):
            return
        self.model.launch_game(self.view.main_frame.game_list_var.get())

    def get_path(self) -> None:
        path: str = fd.askopenfilename(initialdir=self.model.DownloadsFolder)
        self.view.install_frame.path_field_var.set(path)

    def toggle_scenario_checkbutton(self, *_) -> None:
        if self.view.install_frame.scenario_var.get():
            self.view.install_frame.scenario_var.set(False)
        else:
            self.view.install_frame.scenario_var.set(True)
        self.toggle_install_fields()

    def toggle_install_fields(self, *_) -> None:
        states = {True: tk.DISABLED, False: tk.NORMAL}
        fields = self.view.install_frame.name_field, self.view.install_frame.version_field
        state_var = self.view.install_frame.scenario_var.get()
        for field in fields:
            field.configure(state=states[state_var])

    def surface_main(self) -> None:
        self.view.install_frame.pack_forget()
        self.view.main_frame.pack()
        self.reset_fields()

    def surface_installer(self) -> None:
        self.view.main_frame.pack_forget()
        self.view.install_frame.pack()

    def surface_uninstall_confirm(self) -> None:
        self.view.main_frame.pack_forget()
        self.view.confirm_uninstall.pack()

    def reset_fields(self):
        frame = self.view.install_frame
        for attribute, variable in frame.defaults.items():
            getattr(frame, attribute).set(variable)

    def quit(self) -> None:
        self.view.destroy()
