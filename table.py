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
        row_length = len(self.data[0])
        col_length = len(self.data)
        self.size = (col_length, row_length)
        return

    def add_rows(self, num=1):
        row = [0] * self.size[1]
        while num > 0:
            self.data.append(row)
            num -= 1
        self.__calculate_size()
        return

    def add_columns(self, num=1):
        while num > 0:
            for i in range(len(self.data)):
                self.data[i].append(0)
                i += 1
            num -= 1
        self.__calculate_size()
        return

    def print_table(self):
        pprint.pprint(self.data)

    def edit_value(self, x, y, value):
        self.data[x][y] = value


    def mid_row(self, row):
        # можно написать лучше, хз как
        where = self.data[row]
        print(np.mean(where))
        return

    def mid_column(self, col):
        ax = np.mean(self.data, axis=0)
        print(ax[col])
        return

    def sum_row(self, row):
        where = self.data[row]
        print(np.sum(where))
        return

    def sum_column(self, col):
        ax = np.sum(self.data, axis=0)
        print(ax[col])
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