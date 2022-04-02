#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Library to open the csv file (among many other things)
import pandas as pd
from pandas.core.frame import DataFrame
#Library to create random numbers (years in our case):
import random
#Library to manage input arguments of the script:
import argparse



def opera_by_year(fin_n, fout_n):
    """
    Function that given an input and an output CSV files, creates 
    trivial style questions for each row of the input file. The question
    it creates is about the creation year, and it produces two distractors
    for each correct answer.
    """
    #Load the input file into a dataframe (pandas object)
    df = pd.read_csv(fin_n)
    #create an empty list to store the output data (each element one row)
    out_rows = []
    
    #We will create questions and write them on the output file
    for _,row in df.iterrows():
        question = "When was this opera writen? ("+row["name"].strip()+", "+row["author"].strip()+")"
        correct = row["year"]

        #We will create 3 numbers randomly between -50 and 50 
        random_numbers = random.sample(range(-50,51),3)
        #if one of the numbers is 0, we will take it out of the list
        if 0 in random_numbers:
            random_numbers.remove(0)
        #To create the first distractor we add to the correct answer the first random_number
        #Bare in mind that the correct answer is a string, as we read it from a csv file, so we first need to cast it to int
        distractor1 = correct + random_numbers[0]
        #To create the first distractor we add to the correct answer the second random_number
        distrator2 = correct + random_numbers[1]
        out_rows.append([question,correct,distractor1,distrator2])
    #create a DataFrame from the rows for the output
    df_out = DataFrame(out_rows)
    #define the header (column's name)
    fieldnames = ["Question","Correct","Incorrect1","Incorrect2"]
    #write the data in the output file
    df_out.to_csv(fout_n,header=fieldnames,index=False)

#Argparse is a library to manage arguments easily
#we first define the Parser with a description
parser = argparse.ArgumentParser(description="Creates trivial exercises for opera years randomly based on a CSV file.")
#then we define the different arguments: a short name, long name, and a message to help. 
# In addition, it has many options (check the documentation), from which we use the required field. 
parser.add_argument('-i',"--input",help="input file",required=True)
parser.add_argument('-o',"--output",help="output file",required=True)
#Finaly, we parse the arguments, and so, in the args variable will be all the inormation introduced
args = parser.parse_args()

opera_by_year(args.input, args.output)