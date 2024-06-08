from table import ConsoleTable

class ConsoleMenu:
    def __init__(self, help_filename):
        self.__init_help_text(help_filename)
        self.table = ConsoleTable()
        self.active = False
        self.menu_items = {"создать": self.create_table, "открыть": self.open_table, "сохранить": self.save_table,
                           "показать": self.show_table, "добавить строку": self.add_rows,
                           "добавить столбец": self.add_columns, "график столбца": self.graph_col,
                           "среднее в строке": self.mid_row, "среднее в столбце": self.mid_col,
                           "сумма в строке": self.sum_row, "сумма в столбце": self.sum_col,
                           "изменить значение": self.change_cell, "справка": self.help, "выход": self.exit}

    def start(self):
        self.help()
        self.active = True
        while self.active:
            command = input("Команда: ").strip()
            if command in self.menu_items:
                self.menu_items[command]()
            else:
                print('wrong command')

    def create_table(self):
        width = int(input("ширина таблицы: "))
        height = int(input("высота таблицы: "))

        new_row = [[0] * width]
        self.table.data = new_row * height
        return

    def open_table(self):
        filename = input("Введите путь до файла ")
        self.table.read_file(filename)
        return

    def save_table(self):
        filename = input("Введите имя файла ")
        self.table.write_file(filename)
        return

    def show_table(self):
        self.table.print_table()
        return

    def add_rows(self):
        num = int(input("Введите количество строк "))
        self.table.add_rows(num)
        return

    def add_columns(self):
        num = int(input("Введите количество столбцов "))
        self.table.add_columns(num)
        return

    def graph_col(self):
        col = int(input("Введите номер столбца "))
        self.table.graph_from_column(col)
        return

    def mid_row(self):
        row = int(input("Введите номер строки "))
        self.table.mid_row(row)
        return

    def mid_col(self):
        col = int(input("Введите номер столбца "))
        self.table.mid_column(col)
        return

    def sum_row(self):
        row = int(input("Введите номер строки "))
        self.table.sum_row(row)
        return

    def sum_col(self):
        col = int(input("Введите номер столбца "))
        self.table.sum_column(col)
        return

    def change_cell(self):
        y = int(input("Выберите строку "))
        x = int(input("Выберите столбец "))
        value = int(input("Введите значение "))
        self.table.edit_value(x, y, value)
        return

    def __init_help_text(self, h):
        with open(h, 'r', encoding='utf-8') as file:
            self.help_text = file.read()

    def help(self):
        print('О программе:')
        print(self.help_text)
        return

    def exit(self):
        self.active = False
        print("The end")