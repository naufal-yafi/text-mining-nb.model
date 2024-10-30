import os

def base_dir(folder, index=0):
  if folder == 'dataset-sample':
    path_folder = ['1_translated', '2_clear-duplicate']
    return f"src/data/dataset-sample/{path_folder[index]}"
  elif folder == 'preprocessing':
    path_folder = ['1_case-folding', '2_cleaning', '3_filtering', '4_stemming', '5_labeling']
    return f"src/data/preprocessing/{path_folder[index]}"
  else:
    return 'invalid folder'

def join(base_dir, path):
  return os.path.join(base_dir, path)