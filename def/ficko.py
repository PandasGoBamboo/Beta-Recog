import json, csv
import pandas as pd

path = ('../zdf_data/pipapo.csv')

df = pd.read_csv(path, encoding='utf-8', sep=';')

d = df['Attribute']

new = pd.DataFrame()
new['new'] = d.str.capitalize()

new.to_csv('../zdf_data/popapi.csv', encoding='utf-8', sep=';')