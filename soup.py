#!/usr/bin/python
#-------------------------#
#   import data from net  #
#-------------------------#
from urllib.request import urlretrieve
import pandas as pd

url='https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

#save>local
urlretrieve(url, 'winequality-red.csv')

#read>dataFrame+prnt(head)
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
