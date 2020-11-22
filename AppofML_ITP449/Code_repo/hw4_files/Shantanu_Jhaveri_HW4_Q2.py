# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW4
# Question 2

import numpy as np
import pandas as pd

# set up initial frame
frame = pd.read_csv("/Users/shantanujhaveri/Desktop/Class_Archives/AppofML_ITP449/workspace/hw4_files/mtcars.csv")
frame = frame.set_index('Car Name')
frame = frame[['cyl', 'gear', 'hp', 'mpg']].copy()
frame = frame.rename(columns={'cyl': 'Cylinders', 'gear': 'Gear', 'hp': 'Horse Power', 'mpg': 'Miles Per Gallon'})

# create frame Powerful column quanitifier
pwr = frame['Horse Power'] >= 110
frame['Powerful'] = pwr

# drop horse power column
frame2 = frame.drop(columns='Horse Power')

# order based on horsepower and only greater than 25 mpg
frame = frame.drop(frame[frame['Miles Per Gallon'] <= 25].index)
frame = frame.sort_values(by=['Horse Power'], ascending=False)

# remove all other cars except the most powerful
frame = frame[frame.Powerful]

# print car with the largest miles per gallon bc it is already
# sorted by mpg
print(frame.head(1))