import pandas as pd

class DataPreProcessor:
    def __init__(self, file_path, orient):
        self.file_path = file_path
        if file_path.split(".")[-1] == "json":
            self.dataframe = pd.read_json(file_path, orient=orient)
        elif file_path.split(".")[-1] == "csv":
            self.dataframe = pd.read_csv(file_path)

    def get_dataframe(self):
        return self.dataframe