import pandas as pd
import sys

def create(path_file):
  try:
    return pd.read_csv(path_file)
  except Exception as err:
    print(f'Err: {err}\n')
    sys.exit(1)
    
def check_available_column(column_name, dataframe):
  if column_name in dataframe.columns:
    return dataframe
  else:
    print(f"Err: Column {column_name} doesn't exist\n")
    sys.exit(1)

def combine(df1, df2):
  return pd.concat([df1, df2], axis=1)