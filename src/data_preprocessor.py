import pandas as pd

class DataPreProcessor:
    def __init__(self, json_file, orient):
        self.json_file = json_file
        self.data = pd.read_json(json_file, orient=orient)

    def get_dataframe(self):
        return self.data