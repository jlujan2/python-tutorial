import pandas as pd

x = pd.Series([6,4,8,6])
print (x)
x = pd.Series([6,4,8,6], index=["q","w","e","r"])
print(x)

data = {'name':['Tim','Jim','Pam','Sam'],
		'age':[29,31,27,35],
		'ZIP':['02115','02130','67700','001100']}