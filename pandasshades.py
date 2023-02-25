import pandas as pd
df = pd.read_csv('shades.csv')

def fileRead(df):
    return df

def describeStats(df):
    return df.describe()

def getHSV(df):
    return df.head()

print(fileRead(df))
print(describeStats(df))
print(describeStats(df))


