from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values="NaN", strategy="mean")
import pickle
from sklearn.externals import joblib

train = pd.read_csv('/Users/divyarobert/PycharmProjects/docs_parser/data/train.csv')

print(train.head())
col = train.columns
print(train.isna().sum())
# class Preprocessing:
#     def __init__(self, data):
#         self.data = data
#     def preprocess(self):
#         data = self.data
#         train = data.dropna(thresh=2)
#         train = train.drop(['Survived','PassengerId','Cabin', 'Embarked', 'Age', 'Name'], axis=1)
#         train = pd.get_dummies(train)
#         return train

from utils import Preprocessing

pr = Preprocessing(train)
X = pr.preprocess()
print(train.columns)
y = train['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
file = open('model.pkl', 'wb')

pickle.dump(rf, file)
joblib.dump(rf, 'job.pkl')
#file = open('model.pkl', 'rb')
#model = pickle.load(file)
model = joblib.load('job.pkl')
y_pred = model.predict(X_test)
print(f1_score(y_test, y_pred))


