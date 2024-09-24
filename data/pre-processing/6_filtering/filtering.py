import os
from dotenv import load_dotenv
import pandas as pd
from stopwords import load_stopwords, remove_stopwords

load_dotenv()

BASE_DIR = os.getenv('BASE_DIR')

output_path = './data/pre-processing/7_stemming/stemming-aduan-siswa.csv'
input_stopword_path = 'data/pre-processing/6_filtering/stopword-list.txt'
input_csv_path = 'data/pre-processing/6_filtering/filtered-aduan-siswa.csv'

stopword_file = os.path.join(BASE_DIR, input_stopword_path)
csv_file = os.path.join(BASE_DIR, input_csv_path)

try:
  stopwords = load_stopwords(stopword_file)
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')

if 'Aduan' in df.columns:
  try:
    df['Aduan'] = df['Aduan'].apply(lambda text: remove_stopwords(text, stopwords))
    df.to_csv(output_path, index=False)
    
    print(f'Success: filtering, output on {output_path}\n')
  except Exception as err:
    print(f'Err: {err}\n')
else: 
  print("Err: Column 'Aduan' doesn't exist\n")