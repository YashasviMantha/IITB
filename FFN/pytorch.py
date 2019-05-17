import torch
import pandas
from _DUMP import me

me.importfix('C:/Users/Zara/Desktop/Internship/Work/FFN')

input_data = pandas.read_csv('Input.csv',error_bad_lines=False)
print(input_data)
