import pandas as pd

file_name = '2021-22-Q4-Code2'
code_num = int(file_name[-1])
fin_yr = int(file_name[5:7])

data = pd.read_csv(f"{file_name}.csv")

qtr_periods = {
    18: ['30/06/2017', '30/09/2017', '31/12/2017', '31/03/2018'],
    19: ['30/06/2018', '30/09/2018', '31/12/2018', '31/03/2019'],
    20: ['30/06/2019', '30/09/2019', '31/12/2019', '31/03/2020'],
    21: ['30/06/2020', '30/09/2020', '31/12/2020', '31/03/2021'],
    22: ['30/06/2021', '30/09/2021', '31/12/2021', '31/03/2022'],
}


# print(type(qtr_periods[fin_yr][0]))

def pct_response():
    response = data.rename(
        {'%_responses_more_than_15min': qtr_periods[fin_yr][0],
         '%_responses_more_than_15min.1': qtr_periods[fin_yr][1],
         '%_responses_more_than_15min.2': qtr_periods[fin_yr][2],
         '%_responses_more_than_15min.3': qtr_periods[fin_yr][3]},
        axis='columns')
    return pd.melt(response, id_vars='LGA', value_vars=qtr_periods[fin_yr],
                   var_name='Period', value_name='%_responses_more_than_15min')


def avg_response_min():
    response = data.rename(
        {'avg_response_time': qtr_periods[fin_yr][0],
         'avg_response_time.1': qtr_periods[fin_yr][1],
         'avg_response_time.2': qtr_periods[fin_yr][2],
         'avg_response_time.3': qtr_periods[fin_yr][3],
         }, axis='columns')

    return pd.melt(response, id_vars='LGA', value_vars=qtr_periods[fin_yr],
                   var_name='Period', value_name='avg_response_time_min')


def total_first_response():
    response = data.rename(
        {'total_num_first_responses': qtr_periods[fin_yr][0],
         'total_num_first_responses.1': qtr_periods[fin_yr][1],
         'total_num_first_responses.2': qtr_periods[fin_yr][2],
         'total_num_first_responses.3': qtr_periods[fin_yr][3],
         }, axis='columns')
    return pd.melt(response, id_vars='LGA', value_vars=qtr_periods[fin_yr],
              var_name='Period', value_name='total_num_first_responses')

# print(df1)
# print(df2)
# print(df3)

# print(df3[df3.LGA=='Interstate LGAs'])

if code_num == 1:
    result = pd.merge(pct_response(), avg_response_min(), on=["LGA", "Period"])  # Code1
    result = pd.merge(result, total_first_response(), on=["LGA", "Period"])
elif code_num == 2:
    result = pd.merge(avg_response_min(), total_first_response(), on=["LGA", "Period"])

else:
    print("Invalid Code number. Choose 1 or 2.")

# print(result)
# print(result.columns)
# # # print(result[result.LGA=='Alpine'])
result.to_csv(f"{file_name}_melt.csv", mode="w")
