import pandas as pd

a = [1, 2, 3, 4, 5]

b = pd.Series(a, index=['a', 'b', 'c', 'd', 'e']) # Giving Custom Index 

print(b)





# Creating Series:- 




# A) From a List:- 

import pandas as pd

s = pd.Series([1, 2, 3, 4])

print(s)




# B) Custom Index:- 


import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s)




# C) From Dictionary


data = {
    'Math': 90,
    'Science': 85,
    'English': 88
}

s = pd.Series(data)

print(s)





# D) Using Scalar Value (Single Value for all 3 values)


s = pd.Series(100, index=['a', 'b', 'c'])

print(s)








# Accessing Data in Series :- 




# A) By Index Position:- 


s = pd.Series([10, 20, 30])

print(s[0])

# Output:

# 10




# B) By Label


s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s['b'])

# Output:

# 20





# C) Multiple Values


print(s[['a', 'c']])

# Output:

# a    10
# c    30










