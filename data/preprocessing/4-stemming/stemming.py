import os 
from dotenv import load_dotenv
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

load_dotenv()

input_path = 'data/preprocessing/3-filtering/dataset-filtering.csv'
output_path = './data/preprocessing/4-stemming/dataset-stemming.csv'

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, input_path)

try:
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')
  
if 'Aduan' in df.columns:
  try:
    stemmer = StemmerFactory().create_stemmer()
    
    df['Aduan'] = df['Aduan'].apply(lambda x: stemmer.stem(x))
    df.to_csv(output_path, index=False)
    
    print(f'Success: stemming data, output on {output_path}\n')
  except Exception as err:
    print(f'Err: {err}\n')
else: 
  print("Err: Column 'Aduan' doesn't exist\n")