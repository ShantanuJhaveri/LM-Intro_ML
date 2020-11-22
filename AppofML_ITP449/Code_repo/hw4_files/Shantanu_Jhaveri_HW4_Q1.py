# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW4
# Question 1

import numpy as np
import pandas as pd

frame = pd.read_csv("/Users/shantanujhaveri/Desktop/Class_Archives/AppofML_ITP449/workspace/hw4_files/mtcars.csv")
frame = frame.set_index('Car Name')
print(frame)
