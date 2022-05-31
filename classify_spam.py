import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from preprocessing import process_text

df = pd.read_csv('spam.csv', encoding="ISO-8859-1")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.rename(columns={'v1': 'Label', 'v2': 'Mail'}, inplace=True)

print(df['Label'].value_counts())

df['Label'] = df['Label'].map({'ham': 1, 'spam': 0})


df['msg'] = df['Mail'].apply(lambda x: process_text(x))
print(df.head())

