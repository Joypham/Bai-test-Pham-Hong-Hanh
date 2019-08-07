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
