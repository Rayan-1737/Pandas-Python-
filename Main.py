# import pandas as pd

# # print(pd.__version__)

# # a = ["Rayan" , 141 , "Hello"]

# # rayan = pd.Series(b)

# # rayan[["A" , "C"]] = ["Rayan", "Ronak"]

# # print(rayan["A"])

# # rayan.index = index = ["X" , "Y", "Z"]

# b = {"name":"Rayan" , "Age":19 , "RollNo":141}

# rayan = pd.Series(b)

# print(rayan)






import pandas as pd 

a = [10, 25, 30, 5, 50]

rayan = pd.Series(a) 

# rayan.index = index = ["X" , "Y" , "Z" ] 

# print(rayan[rayan>20])

print(rayan.values>20)

