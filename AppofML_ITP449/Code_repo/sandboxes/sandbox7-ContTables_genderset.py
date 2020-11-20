import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo'
                 '/sandboxes/sandbox-data/GenderPurchase.csv')

# CONTINGENCY TABLE: TABLE OF FREQUENCY FOR OBSERVATIONS FALLING UNDER TWO OR MORE VARIABLES
contingencyTable = pd.crosstab(df['Gender'],df['Purchase'])
print(df.shape)
print(contingencyTable)

# SUM OF ROWS AND COLUMNS ON CONTINGENCY TABLE
print(contingencyTable.sum(axis=1))
print(contingencyTable.sum(axis=0))

# CONTINGENCY TABLE AS PERCENTAGES OF GENDER TOTAL
print(contingencyTable.astype('float').div(contingencyTable.sum(axis=1),axis=0))