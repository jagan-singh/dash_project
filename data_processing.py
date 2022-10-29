import pandas as pd
import requests
import io

url = "https://raw.githubusercontent.com/jagansingh93/n_movies/main/n_movies.csv"
download = requests.get(url).content

# Reading file from github
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Dropping nas
df.dropna(inplace = True)

# Processing genre
df['genre'] = df['genre'].str.split(',')

# Getting a column for each genre
for index, row in df.iterrows():
    for x in row['genre']:
        df.at[index, x] = 1   

# Filling emmpty genre with 0
df.fillna(0, inplace = True)
