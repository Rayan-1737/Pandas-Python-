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

# Returns the dimensions of the Series.

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






