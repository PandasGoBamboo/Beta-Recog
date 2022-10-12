import pandas as pd
from datetime import datetime
from collections import Counter



# Datenablageort
file = 'C:/Users/tschu/Desktop/BETA-RECOG/more_raw_data.pkl'

print('Ich roedel......')

startTime = datetime.now()
data = pd.read_pickle(file)

keys = Counter(data['pform']).keys()
values = Counter(data['pform']).values()

d = pd.DataFrame({'Pform': keys,
'Anzahl': values}
)
print(keys)
print(values)
print(datetime.now() - startTime)