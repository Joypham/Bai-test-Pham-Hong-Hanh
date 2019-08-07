# Step 1: Lấy ra 3 thể loại phim phổ biến 

import pandas as pd
from collections import Counter

data_url = 'https://raw.githubusercontent.com/TechMaster/luyen-logic/master/movies.csv'
df = pd.read_csv(data_url)
genre_list = df["genres"].apply(lambda x: x.split('|'))
flat_list = [item for sublist in genre_list for item in sublist]
# Đếm số lượng genre:

counter_genres = Counter(flat_list)
data = pd.Series(counter_genres)

# Lấy ra 3 the loai phim pho bien nhat: Drama, Comedy,Thriller
joy = pd.DataFrame({'genre':data.index, 'count':data.values}).sort_values(by='count',ascending=0).head(3)

print (joy)
