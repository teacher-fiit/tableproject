import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = 'Итоги домашних заданий'
        self.files = {}
        self.gui()

    def gui(self):
        label_csv = tk.Label(self, text='Загрузка файлов *.csv')
        label_csv.pack()
        open_button = tk.Button(self, text='Загрузить результаты ДЗ', command=self.open_file)
        open_button.pack()
        self.text = tk.Text(width=30, height=10)
        self.text.pack()
        label_xls = tk.Label(self, text='Загрузка файла *.xlsx')
        label_xls.pack()
        fio_button = tk.Button(self, text='Добавить фамилии', command=self.add_fio)
        fio_button.pack()
        union_button = tk.Button(self, text='Объединить и сохранить', command=self.union_and_save)
        union_button.pack()

    def add_fio(self):
        pass

    def open_file(self):
        pass

    def union_and_save(self):
        pass


