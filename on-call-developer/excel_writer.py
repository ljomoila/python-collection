import pandas as pd


class ExcelWriter:
    def __init__(self, columns, filename):
        self.filename = filename
        self.columns = pd.DataFrame(columns=columns)

    def add_to_columns(self, index, data):
        self.columns.loc[index] = data

    def write(self):
        self.columns.to_excel(self.filename, index=False)
        print(self.columns)
