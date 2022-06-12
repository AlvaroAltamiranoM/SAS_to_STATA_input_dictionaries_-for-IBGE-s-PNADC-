# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:05:55 2022

@author: unily
"""
import pandas as pd
import os
import csv
anio= 2022
path = r'C:\Users\FILE_PATH'
os.chdir(path)
input = pd.read_csv(r'input_PNADC_trimestral.txt', header=None, encoding = 'latin-1')
input[0] = input[0].str.replace(r"([\@])(\d+)", r"_column (0\2)").astype('str')
input[0] = input[0].str.replace(r"\/\*", '"').astype('str')
input[0] = input[0].str.replace(r"\*\/", '"').astype('str')
input[0] = input[0].str.replace(r"\$", '').astype('str')
input[0] = input[0].str.replace(r"(\d+)(\.)", r"%\1g").astype('str')
input[0].to_csv(r'input_{}_(stata)dict.txt'.format(anio), header=False, index=False, quoting=csv.QUOTE_NONE)
