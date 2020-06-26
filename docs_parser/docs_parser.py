from flask import Flask, Response, jsonify
app = Flask(__name__)
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import pickle
#from utils import Preprocessing
class Preprocessing:
    def __init__(self, data):
        self.data = data
    def preprocess(self):
        data = self.data
        train = data.dropna(thresh=2)
        train = train.drop(['Survived','PassengerId','Cabin', 'Embarked', 'Age', 'Name'], axis=1)
        train = pd.get_dummies(train)
        return train


train = pd.read_csv('/Users/divyarobert/PycharmProjects/docs_parser/data/train.csv')
pr = Preprocessing(train)
X = pr.preprocess()
print(train.columns)
y = train['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
@app.route("/")
def hello():
    test = pd.read_csv('/Users/divyarobert/PycharmProjects/docs_parser/data/train.csv')
    pr = Preprocessing(test)
    X = pr.preprocess()
    #file = open('model.pkl', 'rb')
    #model = pickle.load(file)
    #model = joblib.load('job.pkl')
    pred = rf.predict(X)
    #print(pred)
    return jsonify('The value returned is ' + str(pred[1]) + '| The value returned is ' + str(pred[2]))


if __name__ == "__main__":
    app.run("0.0.0.0", port=90, debug=True)
