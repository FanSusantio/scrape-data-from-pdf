import re
import pandas as pd


def solve(s):
    char_arr = list(s)
    char_arr.sort()
    return char_arr == list(s)


file_name = '2018-19-Q4-Code1'
code_num = int(file_name[-1])

with open(f'{file_name}.txt', 'r') as file:
    # data = file.read()
    data_list = file.readlines()  # The readlines() method returns a list containing each line in the file as a list item.

while "\n" in data_list:
    data_list.remove("\n")  # remove all the items that are blank lines in data

data_list = [i.strip() for i in data_list]  # strips '\n' from each item in list
data_list = [re.split(r" (?=\d)", j) for j in data_list]  # splits the string when the lookahead is a space and a digit


'''
Cleaning the LGA names
# https://stackoverflow.com/questions/25346058/removing-list-of-words-from-a-string
'''

df = pd.DataFrame(data_list)  # convert the list into a dataframe

lga = pd.read_csv("lga.csv")  # created and stored a clean list of LGAs in "lga.csv"
lga_list = lga.LGA.tolist()  # open the list

column_names_code = {1: ['LGA',
                      '%_responses_more_than_15min',
                      'avg_response_time',
                      'total_num_first_responses',
                      '%_responses_more_than_15min',
                      'avg_response_time',
                      'total_num_first_responses',
                      '%_responses_more_than_15min',
                      'avg_response_time',
                      'total_num_first_responses',
                      '%_responses_more_than_15min',
                      'avg_response_time',
                      'total_num_first_responses',
                      'total_num_first_responses',
                      ],
                    2: ['LGA',
                        'avg_response_time',
                        'total_num_first_responses',
                        'avg_response_time',
                        'total_num_first_responses',
                        'avg_response_time',
                        'total_num_first_responses',
                        'avg_response_time',
                        'total_num_first_responses',
                        'total_num_first_responses',
                      ]}

# add the column name labels depending on whether it is Code 1 data or Code 2 data
df.columns = column_names_code[code_num]

data_lga_list = df.LGA.tolist()
clean_data_list = []

# clean out the LGA names of non-sensical characters
for line in data_lga_list:
    word_query = line.split()
    word_result = [word for word in word_query if word in str(lga_list)]  # only put back the substring that are in the lga_list string
    result = ' '.join(word_result)
    clean_data_list.append(result)

print(clean_data_list)
df.LGA = pd.Series(clean_data_list)

print(df)

# saving the dataframe
df.to_csv(f'{file_name}.csv')


