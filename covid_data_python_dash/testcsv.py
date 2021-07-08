import pandas as pd
import csv
import datetime
url ="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

#create a yesterday's date string to use in the new csv file
today = datetime.date.today()

yesterday = today - datetime.timedelta(days=2)

print(yesterday)
yy = str(yesterday)

df = pd.read_csv(url)
df[(df['date'] == yy)].to_csv("update1.csv")

with open('update1.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)

