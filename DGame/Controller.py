import tkinter as tk
from tkinter import filedialog as fd

from Model import Model, Game
from View import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.installed_games: list[str] = []

        self.initialize_frames()
        self.update_list_view()
        self.view.main_frame.pack()

    def main_window(self) -> tk.Tk:
        self.view.title('DGame')
        return self.view

    def initialize_frames(self) -> None:
        # Initialize Main Frame
        # Initialize Main Frame Games List
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

        # Initialize Scenario Checkbox
        self.view.install_frame.scenario_label.bind('<Button-1>', self.toggle_scenario_checkbutton)
        self.view.install_frame.scenario_checkbutton.configure(command=self.toggle_install_fields)

        # Initialize Install Button
        self.view.install_frame.install_button.configure(command=self.install_game)

        # Initialize Install Cancel Button
        self.view.install_frame.cancel_button.configure(command=self.surface_main)

        # Initialize Confirm Uninstall Frame
        # Initialize Cancel Button
        self.view.confirm_uninstall.cancel_button.configure(command=self.surface_main)

        # Initialize Confirm Install Cancel Button
        self.view.confirm_install.cancel_button.configure(command=self.cancel_installation)

        # Initialize confirm Install Continue Button
        self.view.confirm_install.cancel_button.configure(command=self.continue_installation)

    def cancel_installation(self) -> None:
        self.view.confirm_install.confirm_var.set(False)
        self.surface_installer()

    def continue_installation(self) -> None:
        self.view.confirm_install.confirm_var.set(True)

    def switch_buttons_on(self, *_) -> None:
        if self.model.database_is_empty(self.installed_games):
            return
        for button in self.view.main_frame.buttons:
            button['state'] = tk.NORMAL

    def launch_callback(self) -> None:
        if self.model.database_is_empty(self.installed_games):
            return
        self.model.launch_game(self.view.main_frame.game_list_var.get())

    def install_game(self) -> None:
        frame = self.view.install_frame
        path = frame.path_field_var.get()
        if frame.scenario_var.get():
            self.model.install_scenario(path)
        else:
            name = frame.name_field_var.get()
            version = frame.version_field_var.get()
            if self.model.game_in_database(name):
                if not self.confirm_install():
                    return
            self.model.install_game(name, version, path)
        self.update_list_view()
        self.surface_main()

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

    def confirm_install(self) -> bool:
        frame = self.view.install_frame
        game_name = frame.name_field_var.get()
        old_game = self.model.get_game(game_name)
        message = f'A game with the name {game_name} already exists with ' \
                  f'version number {old_game.version}. It was installed ' \
                  f'on {old_game.date}. Overwrite this game?'
        self.view.confirm_install.explanation_var.set(message)
        self.surface_confirm_install()
        return self.view.confirm_install.confirm_var.get()

    def pack_forget(self):
        for frame in self.view.frames:
            frame.pack_forget()

    def surface_main(self) -> None:
        self.pack_forget()
        self.view.main_frame.pack()
        self.reset_fields()

    def surface_installer(self) -> None:
        self.pack_forget()
        self.view.install_frame.pack()
        self.reset_fields()

    def surface_confirm_install(self) -> None:
        self.pack_forget()
        self.view.confirm_install.pack()
        # No self.reset_fields() because that would reset the fields we
        # would need to access to go through the continue flow.

    def surface_uninstall_confirm(self) -> None:
        self.pack_forget()
        self.view.confirm_uninstall.pack()
        self.reset_fields()

    def reset_fields(self):
        for frame in self.view.frames:
            for attribute, variable in frame.defaults.items():
                getattr(frame, attribute).set(variable)

    def update_list_view(self):
        self.view.main_frame.game_list_var.set(self.model.read_game_names())
        self.installed_games = self.view.main_frame.game_list_var.get()

    def quit(self) -> None:
        self.view.destroy()
