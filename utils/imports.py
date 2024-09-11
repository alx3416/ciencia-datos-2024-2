import pandas as pd


class Dataset:
    def __init__(self, path):
        self.dataframe = []
        self.columns = []
        self.rows = []

    def read_data(path):
        return pd.read_csv(path)


class Diabetes(Dataset):
    def __init__(self, path):
        self.dataframe = []
        self.columns = 11
        self.rows = 442

    def read_data(path):
        return pd.read_csv(path, sep="/t")

df = Diabetes("data/diabetes.tab.txt")

print(df.rows)
print(df.columns)
