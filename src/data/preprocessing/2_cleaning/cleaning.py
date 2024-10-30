from package.path import base_dir, join
from package.dataframe import check_available_column, create
from package.env import get_env
from package.system import error, exit
from package.text import clean_text

input_path = f"{base_dir('preprocessing', 0)}/case-folding-dataset.csv"
output_path = f"{base_dir('preprocessing', 1)}/cleaning-dataset.csv"

csv_file = join(get_env('BASE_DIR'), input_path)

df = check_available_column('Aduan', create(csv_file))

try:
  df['Aduan'] = df['Aduan'].apply(clean_text)
  df.to_csv(output_path, index=False)
  exit(f"Success: case folding, output on {output_path}\n")
except Exception as err:
  error(err)