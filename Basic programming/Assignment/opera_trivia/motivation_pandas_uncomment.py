#!/usr/bin/python3
# -*- coding: utf-8 -*-

# WILL NOT WORK WITH THE RUN BUTTON ON VISUAL STUDIO CODE!
# USE THE TERMINAL:
# python3 motivation_pandas_uncomment.py -i your_input_file -o your_output_file

import pandas as pd
from pandas.core.frame import DataFrame

import random
import argparse

def opera_by_year(fin_n, fout_n):
    """
    Function that given an input and an output CSV files, creates 
    trivial style questions for each row of the input file. The question
    it creates is about the creation year, and it produces two distractors
    for each correct answer.
    """

    df = pd.read_csv(fin_n)
    out_rows = []

    for _,row in df.iterrows():

        question = "When was this opera writen? ("+row["name"].strip()+", "+row["author"].strip()+")"
        correct = row["year"]
        random_numbers = random.sample(range(-50,51),3)

        if 0 in random_numbers:
            random_numbers.remove(0)

        distractor1 = correct + random_numbers[0]
        distrator2 = correct + random_numbers[1]
        out_rows.append([question,correct,distractor1,distrator2])

    df_out = DataFrame(out_rows)
    fieldnames = ["Question","Correct","Incorrect1","Incorrect2"]
    df_out.to_csv(fout_n,header=fieldnames,index=False)

parser = argparse.ArgumentParser(description="Creates trivial exercises for opera years randomly based on a CSV file.")
parser.add_argument('-i',"--input",help="input file",required=True)
parser.add_argument('-o',"--output",help="output file",required=True)

args = parser.parse_args()

opera_by_year(args.input, args.output)