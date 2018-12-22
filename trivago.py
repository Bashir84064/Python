import os
import numpy as np
import pandas as pd
from pandas import *

df = pd.read_csv('hotels.csv',encoding='utf-8')
df['updated_stars']=df[(df['stars']<=5) & (df['stars']>=0)]['stars']
df.drop('stars',axis=1,inplace=True)
sum(df['uri'].apply(lambda name:name[7:10]=='www'))
df['uri_new'] = df[df['uri'].apply(lambda name:name[7:10]=='www')]['uri']
df.drop('uri',axis=1,inplace=True)
df['uri_new'].fillna("URL not_available",inplace=True)
df.head()

def to_1xml(df, filename=None, mode='w'):
    def row(row):
        xml = ['<resp>']
        for i, col_name in enumerate(row.index):
            xml.append('  <invent name="{0}">{1}</invent>'.format(col_name, row.iloc[i]))
        xml.append('</resp>')
        return '\n'.join(xml)
    out = '\n'.join(df.apply(row, axis=1))

    if filename is None:
        return out
    with open(filename, mode) as f:
        f.write(out)

pd.DataFrame.to_xml = to_1xml
df.to_xml('hotels.xml')
print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

df.to_html('hotels.html')
