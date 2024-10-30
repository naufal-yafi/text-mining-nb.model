from package.path import base_dir, join
from package.dataframe import combine,check_available_column, create
from package.env import get_env
from package.system import error, exit

input_path = f"{base_dir('preprocessing', 3)}/stemming-dataset.csv"
output_path = "./dist/accurate-dataset.csv"
label_path = f"{base_dir('preprocessing', 4)}/label.csv"

aduan_file = join(get_env('BASE_DIR'), input_path)
label_file = join(get_env('BASE_DIR'), label_path)

df_aduan = check_available_column('Aduan', create(aduan_file))
df_label = check_available_column('Label', create(label_file))

try:
  df = combine(df_aduan, df_label)
  df.to_csv(output_path, index=False)
  exit(f"Success: preprocessing data, output on {output_path}\n")
except Exception as err:
  error(err)