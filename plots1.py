import pandas as pd

url='http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'


#read all sheets
xls = pd.read_excel(url, sheet_name=None)

#prnt sheetnames
print(xls.keys())

#prnt hd of 1stsheet(name, not index)
print(xls['1700'].head())
