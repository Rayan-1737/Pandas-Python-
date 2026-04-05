import pandas as pd

a = {'Cows': [12, 20], 'Goats': [22, 19]},

animals = pd.DataFrame(a ,  index=['Year 1', 'Year 2'])

animals.to_csv("cows_and_goats.csv")

