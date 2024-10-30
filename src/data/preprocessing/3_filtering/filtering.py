from package.path import base_dir, join
from package.env import get_env
from package.dataframe import check_available_column, create
from package.stopwords import load, removing_text
from package.system import error, exit

# csv
input_path = f"{base_dir('preprocessing', 1)}/cleaning-dataset.csv"
output_path = f"{base_dir('preprocessing', 2)}/filtering-dataset.csv"

#stopword
stopword_path = f"{base_dir('preprocessing', 2)}/stopword-list.txt"

csv_file = join(get_env('BASE_DIR'), input_path)
stopword_file = join(get_env('BASE_DIR'), stopword_path)

df = check_available_column('Aduan', create(csv_file))
sw = load(stopword_file)

try:
  df['Aduan'] = df['Aduan'].apply(lambda text: removing_text(text, sw))
  df.to_csv(output_path, index=False)
  exit(f"Success: filtering, output on {output_path}\n")
except Exception as err:
  error(err)