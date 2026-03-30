import pandas as pd

# Testing auto-sync feature - March 30, 2026

# a = [1,2,3]

# rayan = pd.Series(a)

# rayan.index = index = ['X' , 'Y' , 'Z']

rayan = pd.Series([10,50,20,30,40])

rayan.index = index = ['A' , 'B' , 'C' , 'D' , 'E']

print(rayan.sort_values())

