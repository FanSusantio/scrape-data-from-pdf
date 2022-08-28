'''
This script identifies errors in the data
'''

import pandas as pd

file_name = '2021-22-Q4-Code1'
code_num = int(file_name[-1])

df = pd.read_csv(f"{file_name}.csv")

def percentage_check(column_name):
    ser = df[column_name]
    for i in ser:
        try:
            j = float(i.replace("%", "")) / 100
            if j >=1:
                row = df.loc[ser == i].index
                print(df.LGA.loc[row])
                print(i)

        except ValueError:
            row = df.loc[ser == i].index
            print(df.LGA.loc[row])
            print(i)
            # print(ser)

def time_check(column_name):
    avg_time_check = df[column_name]

    for i in avg_time_check:
        try:
            if len(i) > 5 or not ":" in i:
                row = df.loc[avg_time_check == i].index
                print(df.LGA.loc[row])
                print(i)
                # print(avg_time_check)
        except ValueError:
            print(f"there is a value error at {i}")

def num_check(column_name):
    total_num_check = df[column_name]

    for i in total_num_check:
        try:
            i = int(i.replace(",", ""))

        except ValueError:
            row = df.loc[total_num_check == i].index
            print(df.LGA.loc[row])
            print(i)
            # print(total_num_check)



for i in range(0,4):
    if i == 0:
        percentage_check(f"%_responses_more_than_15min")
        # time_check(f"avg_response_time")
        # num_check(f"total_num_first_responses")
    else:
        percentage_check(f"%_responses_more_than_15min.{i}")
        # time_check(f"avg_response_time.{i}")
        # num_check(f"total_num_first_responses.{i}")
