import pandas as pd
import numpy as np

data = {'ReleaseYear': [2009, 2019, 2015, 2013, 2005],
        'Movie': ['Avatar', 'Avengers:Endgame', "Start Wars", 'Frozxen', 'HP andteh GObvlet of fire'],
        'Expense': [32, 47, 38, 24, 20],
        'Profit': [14, 10, 84, 79, 78]}

df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
# df['Ones'] = 1
# df['IsOld'] = df['ReleaseYear'] < 2015




print(df)