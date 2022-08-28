import pandas as pd
code_num = 2
fin_yr_list = ['2017-18',
               '2018-19',
               '2019-20',
               '2020-21',
               '2021-22']

frames = []

for i in fin_yr_list:
    df = pd.read_csv(f"{i}-Q4-Code{code_num}_melt.csv")
    frames.append(df)

# print(frames)

vertical_stack = pd.concat(frames, axis=0, ignore_index=True)
vertical_stack = vertical_stack.drop('Unnamed: 0', axis=1)
# print(vertical_stack.head())
vertical_stack.to_csv(f"stacked_data_Code{code_num}.csv", mode="w")