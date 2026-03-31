import pandas as pd

a = {
    
    "name":['A','B','C','D','E'],
    "Age":[18 , 64 , 35 , 76 , 54]
     
    }

rayan = pd.DataFrame(a)

# rayan.index = index = ['A' , 'B' , 'C' , 'D' , 'E']

print(rayan.columns) 

