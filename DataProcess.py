import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].valus
Y = dataset.iloc[:, 3].valus

