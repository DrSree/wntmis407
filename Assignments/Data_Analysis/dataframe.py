# Create a new python script to do the following;
#
# Identify and download an open source data file from data.gov (e.g., Consumer Complaints) that is in the csv format. Read the file into a dataframe of pandas. Select one or more rows or columns and print the contents. Show the print results. Pull the script and printed results.
#
# Note: you will need to use pandas package. Also, you must use encoding = 'latin1' if you use python 3.4
# For example,
# df = pd.read_csv(filename, encoding='latin1')
# where pd is the short form use of pandas (e.g., import pandas as pd) and df is a variable of type dataframe.

import pandas as pd

print "Reading Titanic Data...\n"

url = 'https://raw.githubusercontent.com/MIS407/Data_Analysis/master/Data/Titanic_train.csv'
titanic_info = pd.read_csv(url)

print "Suriving Female Passengers"
passengers = titanic_info.query('Sex == "female" and Survived == 1')
print passengers

print "Close Titanic datafile.\n"
