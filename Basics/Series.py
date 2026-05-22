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









# Important Attributes of Series :- 



# A) .index 


print(s.index)

# Gives indexes , .index returns the labels (row names) of the Series.






# B) .values 


print(s.values)

# Returns only the data values as a NumPy array. It removes indexes and keeps raw data.




# C) .dtype


print(s.dtype)

# Shows the data type of the Series values





# D) .shape


print(s.shape)

# Output:-  (3,)

# Returns the dimensions of the Series. Returns the number of rows and columns  ex:-  (3 , 2) means 3 rows and 2 cloumns 

# A Series is 1-dimensional.

# (3,) means:

# 3 elements
# 1 dimension





# E) .size

print(s.size)

# Output:-  3

# Returns total number of elements.









# Series Data Types:- 



# Integer

pd.Series([1, 2, 3])


# Float

pd.Series([1.5, 2.5, 3.5])


# String

pd.Series(["A", "B", "C"])


# Boolean

pd.Series([True, False, True])


# Mixed Type

pd.Series([1, "A", True])
# But mixed types are usually slower.










# Mathematical Operations :- 


# Addition

s = pd.Series([1, 2, 3])

print(s + 10)

# Output:

# 0    11
# 1    12
# 2    13
# dtype: int64



# Multiplication

# print(s * 2)



# Power

# print(s ** 2)









# Series with NumPy-Like Operations:-


# Sum
print(s.sum())

# Mean
print(s.mean())

# Max
print(s.max())

# Min
print(s.min())

# Standard Deviation
print(s.std())








# Updating Values:- 


# Single Value
s[0] = 100


# Multiple Values
s[s > 20] = 999







# Missing Values in Series:- 

# Missing values are represented using NaN.

import numpy as np

s = pd.Series([1, 2, np.nan, 4])

print(s)

# Output:

# 0    1.0
# 1    2.0
# 2    NaN
# 3    4.0
# dtype: float64










# Handling Missing Values

# Check Missing Values
print(s.isnull())

# or

print(s.isna())


# Remove Missing Values
print(s.dropna())



# Fill Missing Values
print(s.fillna(0))






# Important Methods in Series


# A) head()

# Shows first rows.

s.head()




# B) tail()

# Shows last rows.

s.tail()




# C) describe()

# Gives statistics.

s.describe()

# Output includes:

# count
# mean
# std
# min
# max




# D) unique()

# Unique values.

s.unique()




# E) nunique()

# Count unique values.

s.nunique()




# F) value_counts()

# Frequency count.

s.value_counts()

# Very useful.

# Example:

s = pd.Series(['A', 'B', 'A', 'C', 'A'])

print(s.value_counts())

# Output:

# A    3
# B    1
# C    1





# G) sort_values()

# Sort by values.

s.sort_values()





# H) sort_index()

# Sort by index.

s.sort_index()





# I) astype()

# Change datatype.

s.astype(float)




# J) copy()

# Creates copy.

s2 = s.copy()





# A) .info()

# Gives summary information about the Series.

s.info()

# Output includes:

# class type
# total entries
# index range
# non-null values count
# data type
# memory usage






# Indexing Methods:- 


# A) loc[] → label-based
s.loc['a']


# B) iloc[] → position-based
s.iloc[0]





