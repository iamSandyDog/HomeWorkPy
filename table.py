import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import pprint

class ConsoleTable:
    def __init__(self, data=None):
        self.__init_data(data)

    def __init_data(self, data):
        if data == None:
            data = [[0]]
        else:
            longestFrame = 0
            for row in data:
                i = data.index(row)
                if len(data[i]) > longestFrame:
                    longestFrame = len(data[i])
                i += 1

            for row in data:
                i = data.index(row)
                while len(data[i]) != longestFrame:
                    data[i].append(0)
                i += 1
        self.data = data
        self.__calculate_size()
        return

    def __calculate_size(self):
        self.size = (len(self.data), len(self.data[0]))
        return

    def add_rows(self, num=1):
        row = [0] * self.size[1]
        while num > 0:
            self.data.append(row)
            num -= 1
        self.__calculate_size()
        return

    def add_columns(self, num=1):
        for i, row in enumerate(self.data):
            for k in range(num):
                self.data[i].append(0)
        self.__calculate_size()
        return

    def print_table(self):
        pprint.pprint(self.data)

    def edit_value(self, x, y, value):
        if x > 0 and y > 0 and (self.size[0] >= y and self.size[1] >= x):
            self.data[x-1][y-1] = value
        else:
            print("Ячейка не существует")

    def mid_row(self, row):
        if 0 < row <= self.size[0]:
            print(np.mean(self.data[row-1]))
        else:
            print("Ячейка не существует")
        return

    def mid_column(self, col):
        if 0 < col <= self.size[1]:
            ax = np.mean(self.data, axis=0)
            print(ax[col-1])
        else:
            print("Ячейка не существует")
        return

    def sum_row(self, row):
        if 0 < row <= self.size[0]:
            print(np.sum(self.data[row-1]))
        else:
            print("Ячейка не существует")
        return

    def sum_column(self, col):
        if 0 < col <= self.size[1]:
            ax = np.sum(self.data, axis=0)
            print(ax[col - 1])
        else:
            print("Ячейка не существует")
        return

    def write_file(self, filename):
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False, header=False)
        return

    def read_file(self, filename):
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            array = [row for row in reader]
            new_list = []
            for inner_list in array:
                temp_list = []
                for i in inner_list:
                    temp_list.append(self.stringToNumber(i))
                new_list.append(temp_list)
        self.data = new_list
        self.__calculate_size()
        return

    def stringToNumber(self, s):
        try:
            float(s)
            return float(s)
        except ValueError:
            return 0

    def graph_from_column(self, col):
        df = pd.DataFrame(self.data)
        colomn = df.loc[:, col]
        plt.plot(colomn, label=f'Столбец №{col}')
        plt.legend()
        plt.ylabel("Значение параметра")
        plt.show()