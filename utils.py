import pandas as pd
class Preprocessing:
    def __init__(self, data):
        self.data = data
    def preprocess(self):
        data = self.data
        train = data.dropna(thresh=2)
        train = train.drop(['Survived','PassengerId','Cabin', 'Embarked', 'Age', 'Name'], axis=1)
        train = pd.get_dummies(train)
        return train
