from Controller import Controller
from DGame import View


def main():
    controller = Controller()
    app = View.MainWindow(controller)
    app.master.title('DGame')
    app.mainloop()


if __name__ == '__main__':
    main()
