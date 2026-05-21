import pandas as pd

a = [1, 2, 3, 4, 5]

b = pd.Series(a)

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





