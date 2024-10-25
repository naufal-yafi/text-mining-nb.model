import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

input_path = 'data/preprocessing/4-stemming/dataset-stemming.csv'
output_path = './dist/new-dataset.csv'
label_path = 'data/preprocessing/5-labeling/label.csv'

BASE_DIR = os.getenv('BASE_DIR')

aduan_file = os.path.join(BASE_DIR, input_path)
label_file = os.path.join(BASE_DIR, label_path)

df_aduan = pd.read_csv(aduan_file)
df_label = pd.read_csv(label_file)

try:
  combine = pd.concat([df_aduan, df_label], axis=1)
except Exception as err:
  print(f'Err: {err}\n')
  
try:
  combine.to_csv(output_path, index=False)
    
  print(f'Success: preprocessing data, output on {output_path}\n')
except Exception as err:
  print(f'Err: {err}\n')