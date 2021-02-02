import argparse
import pandas as pd
import json
import numpy as np
import os

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="""
  This script is going to convert .csv to .xml. 
  """)
  parser.add_argument("input", help=".csv file")
  args = parser.parse_args()

  input_file_name = args.input

  # Creating output directory
  if not os.path.exists('./output'):
    os.makedirs('./output')

  lib_df = pd.read_csv(input_file_name, index_col= 0)
  columns = list(lib_df) 
  for column in columns: 
    translation_dict = {}
    translation_dict['translations'] = []
    translation_df = lib_df[column][:] 
    for index, value in translation_df.iteritems():
      if not (pd.isnull(value)):
        translation_dict['translations'].append({"key": f"{index}", "value": f"{value}"})
    with open(f'./output/{column}.json', 'w') as json_file:
      json.dump(translation_dict, json_file, ensure_ascii=False)
