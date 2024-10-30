from package.path import base_dir, join
from package.env import get_env
from package.dataframe import create, check_available_column
from package.system import error, exit

input_path = f"{base_dir('dataset-sample', 0)}/translated-dataset.csv"
output_path = f"{base_dir('dataset-sample', 1)}/clear-duplicate-dataset.csv"

csv_file = join(get_env('BASE_DIR'), input_path)

df = check_available_column('Translate', create(csv_file))

try:
  drop_duplicate = df.drop_duplicates(subset='Translate')
  rename_column = drop_duplicate.rename(columns={'Translate': 'Aduan'})
  rename_column.to_csv(output_path, index=False)
  
  exit(f"Success: csv has clear duplicate text, output on {output_path}\n", 0)
except Exception as err:
  error(err)