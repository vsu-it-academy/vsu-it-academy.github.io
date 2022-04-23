from tkinter import *
from tkinter import messagebox
import Settings as settings

class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Меню")

        window_w = 220
        window_h = 260

        w = self.root.winfo_screenwidth()
        print(w)
        h = self.root.winfo_screenheight()
        print(h)
        w = int(w//2 -window_w//2)
        print(w)
        h = int(h//2 - window_h//2)
        print(h)
        self.root.geometry('{}x{}+{}+{}'.format(window_w,window_h,w, h))
        
        self.draw_menu() # отрисовка кнопок и т.д меню

        self.root.mainloop()

    def draw_menu(self):
        colorDefault = "#F5DEB3"

        self.labelName = Label(text="Введите имя игрока:")
        self.labelName.pack(padx=4,pady=4, fill=X)

        self.txtName = Entry()
        self.txtName.pack(padx=4,pady=4, fill=X)

        self.labelLevel = Label(text="Стартовый уровень:")
        self.labelLevel.pack(padx=4,pady=4, fill=X)

        self.txtLevel = Entry()
        self.txtLevel.insert(0,"0")
        self.txtLevel.pack(padx=4,pady=4)

        self.startButton = Button(text="Запустить игру", background=colorDefault, command=self.commandStart)
        self.startButton.pack(padx=4,pady=4, fill=X)

        self.resultButton = Button(text="Лучший результат", background=colorDefault, command=self.commandResultInfo)
        self.resultButton.pack(padx=4,pady=4, fill=X)

        self.developerInfoButton = Button(text="О разработчике", background=colorDefault, command=self.commandDeveloperInfo)
        self.developerInfoButton.pack(padx=4,pady=4, fill=X)

        self.quitButton = Button(text="Закрыть игру", background=colorDefault, command=self.commandQuit)
        self.quitButton.pack(padx=4,pady=4, fill=X)

    def setSittings(self):
        settings.name_player = self.txtName.get()
        settings.start_level = int(self.txtLevel.get())

    def commandQuit(self):
        quit()# закрыть приложение

    def commandStart(self):
        self.setSittings() # применение настроек
        self.root.destroy() # разрушение окна
        self.root.quit() # закрыть приложение

    def commandResultInfo(self):
        messagebox.showinfo( "Лучший результат", "Шидловская Диана, Очки: 20")

    def commandDeveloperInfo(self):
        messagebox.showinfo( "Информация оразработчике", "Я разработчик на Python")