import pandas as pd
import os

data = {'Name':['Gaurav','Nirav', 'Alice'],
        'Age':[25,30,35],
        'City':['New York','Los Angeles','Chicago']}

df = pd.DataFrame(data)

# Adding new row to df for V2
new_row = {'Name':'GF1','Age':20,'City':'City1'}
df.loc[len(df.index)] = new_row

## Adding new row to df for V3
# new_row2= {'Name':'V3','Age':20,'City':'City1'}
# df.loc[len(df.index)] = new_row2

data_dir = "data"
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")