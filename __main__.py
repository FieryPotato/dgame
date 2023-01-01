from DGame.Model import Model
from DGame.View import View
from DGame.Controller import Controller


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    app = controller.main_window()
    app.mainloop()


if __name__ == '__main__':
    main()
