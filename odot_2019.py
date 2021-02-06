import pandas
import matplotlib
import urllib3

df = pandas.read_csv('/Users/trevorjohnson/Documents/Portland State/DATA_ENG/lab3/Oregon Hwy 26 Crash Data for 2019 - Crashes on Hwy 26 during 2019.csv')

for index, row in df.iterrows():
    print(row)
