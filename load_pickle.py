import pandas as pd
from datetime import datetime


# Datenablageort
file = 'C:/Users/tschu/Desktop/BETA-RECOG/raw_data.pkl'

print('Ich roedel......')

startTime = datetime.now()
data = pd.read_pickle(file)

print(data.info)

print(datetime.now() - startTime)