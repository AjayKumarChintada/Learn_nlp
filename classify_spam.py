import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from preprocessing import *

df = pd.read_csv('spam.csv', encoding="ISO-8859-1")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.rename(columns={'v1': 'Label', 'v2': 'Mail'}, inplace=True)

print(df['Label'].value_counts())

df['Label'] = df['Label'].map({'ham': 1, 'spam': 0})


df['Mail'] = df['Mail'].apply(lambda x: remove_punctuations(x))
# df['Mail'] = df['Mail'].apply(lambda x: x.lower())
df['Mail'] = df['Mail'].apply(lambda x: lower_case(x))



print(df.head())

