# messing_with_manipulation.pt
# Author: Rachel King

import pandas as pd
import numpy as np
#import dataManipulation

filename = 'originalData.tsv'

df = pd.read_table(filename)
list_of_cols = ['Module ID', 'Duration']
print(df[list_of_cols].head(2))

df['new'] = df['Duration'] * df['Number of Weeks']

list_of_cols = ['Number of Weeks', 'Duration', 'new']
print(df[list_of_cols].head(10))