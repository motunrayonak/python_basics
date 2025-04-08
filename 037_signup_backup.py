import pandas as pd

my_file=pd.read_json("035_signup_data.json")

my_file.to_excel("038_first_exam_result.xlsx",index=4)

print(my_file)
