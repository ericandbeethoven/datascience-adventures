#!/usr/bin/env python3

import json
import pandas as pd

d = json.load(open('Recidivism_IPC_Crimes_2013.json'))
df = pd.DataFrame(d['data'],
                  columns=[i['label'] for i in d['fields']])

del d
print("SAMPLE:\n",df.ix[0])
print("\n=======\nDESCRIBE:")
print(df.describe())
