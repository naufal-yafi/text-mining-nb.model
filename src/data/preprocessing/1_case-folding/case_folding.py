from package.path import base_dir, join
from package.dataframe import check_available_column, create
from package.system import error, exit
from package.env import get_env

input_path = 'src/data/raw/dataset.csv'
output_path = f"{base_dir('preprocessing', 0)}/case-folding-dataset.csv"

csv_file = join(get_env('BASE_DIR'), input_path)

df = check_available_column('Aduan', create(csv_file))

try:
  df['Aduan'] = df['Aduan'].str.lower()
  df.to_csv(output_path, index=False)
  exit(f"Success: case folding, output on {output_path}\n")
except Exception as err:
  error(err)