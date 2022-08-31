import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd
import tablelib


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
        filename = fd.askopenfilename(filetypes=[("EXCEL files", "*.xlsx")])
        if filename.endswith('xls') or filename.endswith('xlsx'):
            data_fio = pd.read_excel(filename)
            self.sort_data_fio = data_fio.sort_values(by='login')

    def open_file(self):
        filenames = fd.askopenfilenames(filetypes=[("CSV files", "*.csv")])
        for filename in filenames:
            if not filename in self.files.keys():
                k1 = filename.rfind('-')
                k2 = filename.rfind('.')
                number = filename[k1 + 1:k2]
                self.files[filename] = tablelib.get_table(filename, 'Score' + number)
                k = filename.rfind('/')
                filename = filename[k + 1:]
                self.text.insert(1.0, filename + '\n')

    def union_and_save(self):
        self.union_docs()
        self.save_file()
        self.destroy()

    def union_docs(self):
        file_keys = list(self.files.keys())
        res = self.files[file_keys[0]]
        for k in file_keys[1:]:
            res = tablelib.merge_table(res, self.files[k])
        columns = res.columns[1:]
        res['result'] = res[columns[0]]
        for e in columns[1:]:
            res['result'] += res[e]
        self.res = res
        if not self.res.empty:
            d = self.__dict__
            if 'sort_data_fio' in d:
                self.res = tablelib.merge_table(self.res, self.sort_data_fio)

    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("EXCEL files", "*.xlsx")])
        sort_res = self.res.sort_values(by='result', ascending=False)
        if not (filename.endswith('.xlsx') or filename.endswith('.xls')):
            filename += ".xlsx"
        with pd.ExcelWriter(filename) as writer:  # doctest: +SKIP
            sort_res.to_excel(writer, sheet_name='Sheet1')
