import yaml
import pandas as pd
import os
import numpy as np

dectector_file = 'my_config_ave-merge'
grainsout_rel_dir = 'Ruby_Practice'

with open('.'.join([dectector_file,'yml']), 'r') as file:
    dectector_file_data = yaml.safe_load(file)

#print(dectector_file_data)

grainsout_full_dir = '/'.join([os.getcwd(),grainsout_rel_dir,'grains.out'])

#print(grainsout_full_dir)

df_grainsout = pd.read_csv(grainsout_full_dir, sep=" +", engine='python')
cols = df_grainsout.columns[2:]
df_grainsout = df_grainsout.dropna(axis=1)
df_grainsout.columns = cols

#print(df_grainsout)

print(df_grainsout.head())

grains_ids = df_grainsout.loc[:,'ID']

orientations = []
positions = []
for index, row in df_grainsout.iterrows():
    #print(row["exp_map_c[0]"],)
    orientations.append([row["exp_map_c[0]"],row["exp_map_c[1]"],row["exp_map_c[2]"]])
    positions.append([row["t_vec_c[0]"],row["t_vec_c[1]"],row["t_vec_c[2]"]])

print(dectector_file_data['calibration_crystal'])

print('TYPE---------------')
print(type(np.asarray(orientations[0]).tolist()))
print('TYPE---------------')


for id in grains_ids:
    dectector_file_data['calibration_crystal'][id]['orientation'] = np.asarray(orientations[id]).tolist()
    dectector_file_data['calibration_crystal'][id]['position'] = np.asarray(positions[id]).tolist()

print(dectector_file_data['calibration_crystal'])

fileo = open('_'.join([dectector_file,'updated_3','.yml']),'w')

yaml.dump(dectector_file_data, fileo, default_flow_style=False, sort_keys=False)