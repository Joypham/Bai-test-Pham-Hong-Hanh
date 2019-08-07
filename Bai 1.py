import pandas as pd
import matplotlib.pyplot as plt

data_url = 'https://raw.githubusercontent.com/TechMaster/luyen-logic/master/movies.csv'
df = pd.read_csv(data_url)
genre_list = df["genres"].apply(lambda x: x.split('|'))
flat_list = [item for sublist in genre_list for item in sublist]
counter_genres = Counter(flat_list)
print(counter_genres)
