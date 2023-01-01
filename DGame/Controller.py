import tkinter as tk

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

        # Initialize Install Frame
        # Initialize Cancel Button
        self.view.add_frame.cancel_button.configure(command=self.surface_main)

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

    def surface_main(self) -> None:
        self.view.add_frame.pack_forget()
        self.view.main_frame.pack()

    def surface_installer(self) -> None:
        self.view.main_frame.pack_forget()
        self.view.add_frame.pack()

    def surface_uninstall_confirm(self) -> None:
        self.view.main_frame.pack_forget()
        self.view.confirm_uninstall.pack()
