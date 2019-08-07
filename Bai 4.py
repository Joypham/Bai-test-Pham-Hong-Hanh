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


# Step 2: Với mỗi loại genre vừa lấy ra ở Step 1 (Drama, Comedy,Thriller), vẽ đồ thị mô tả tăng giảm của thể loại genre tương ứng  qua các năm

# File 1: Drama_line_chart
import pandas as pd
import matplotlib.pyplot as plt

data_url = 'https://raw.githubusercontent.com/TechMaster/luyen-logic/master/movies.csv'
df = pd.read_csv(data_url)
# Xử lý dữ liệu: Lấy ra dữ năm sản xuất sau khi cắt đi ký tự trống

df["get_year"] = df["title"].str.strip().apply(lambda x: x[-5:-1])
# Lọc ra phim có chứa thể loại là Drama

drama_genre= df[df['genres'].str.contains("Drama")]

# Xử lý dữ liệu lỗi: drop các dòng có năm sản xuất không phải dạng numeric :

joy = drama_genre[drama_genre['get_year'].apply(lambda x: x.isnumeric())]
# group by theo năm sản xuất và đếm số lượng gerne tương ứng

meobeo = joy.astype({"get_year": int}).groupby('get_year').size()
# Vẽ đồ thị:
meobeo.plot.line()
plt.show()
print(meobeo)


# File 2: Thriller_line_chart

import pandas as pd
import matplotlib.pyplot as plt

data_url = 'https://raw.githubusercontent.com/TechMaster/luyen-logic/master/movies.csv'
df = pd.read_csv(data_url)
# Xử lý dữ liệu: Lấy ra dữ năm sản xuất sau khi cắt đi ký tự trống

df["get_year"] = df["title"].str.strip().apply(lambda x: x[-5:-1])
# Lọc ra phim có chứa thể loại là Thriller

drama_genre= df[df['genres'].str.contains("Thriller")]

# Xử lý dữ liệu lỗi: drop các dòng có năm sản xuất không phải dạng numeric :

joy = drama_genre[drama_genre['get_year'].apply(lambda x: x.isnumeric())]
# group by theo năm sản xuất và đếm số lượng gerne tương ứng

meobeo = joy.astype({"get_year": int}).groupby('get_year').size()
# Vẽ đồ thị:
meobeo.plot.line()
plt.show()
print(meobeo)

# File 3: Comedy_line_chart

import pandas as pd
import matplotlib.pyplot as plt

data_url = 'https://raw.githubusercontent.com/TechMaster/luyen-logic/master/movies.csv'
df = pd.read_csv(data_url)
# Xử lý dữ liệu: Lấy ra dữ năm sản xuất sau khi cắt đi ký tự trống

df["get_year"] = df["title"].str.strip().apply(lambda x: x[-5:-1])
# Lọc ra phim có chứa thể loại là Comedy

drama_genre= df[df['genres'].str.contains("Comedy")]

# Xử lý dữ liệu lỗi: drop các dòng có năm sản xuất không phải dạng numeric :

joy = drama_genre[drama_genre['get_year'].apply(lambda x: x.isnumeric())]
# group by theo năm sản xuất và đếm số lượng gerne tương ứng

meobeo = joy.astype({"get_year": int}).groupby('get_year').size()
# Vẽ đồ thị:
meobeo.plot.line()
plt.show()
print(meobeo)


  
