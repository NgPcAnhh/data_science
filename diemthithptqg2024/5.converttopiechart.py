import matplotlib.pyplot as plt
import sqlalchemy as sa

# Khai báo thông tin kết nối database
engine = sa.create_engine(
    "mssql+pyodbc://sa:123456789@DESKTOP-L9G0DQ6/phantichdiemthi?driver=ODBC+Driver+17+for+SQL+Server"
)

# Xác định tên bảng
table_name = "ketquathithptqg"

# Các câu lệnh SQL để lấy dữ liệu
sql_queries1 = {
    "Toán giỏi": f"SELECT COUNT(*) FROM {table_name} WHERE Toán >= 8 AND Toán <> -1",
    "Toán TB": f"SELECT COUNT(*) FROM {table_name} WHERE Toán >= 5 AND Toán < 8 AND Toán <> -1",
    "Toán yếu": f"SELECT COUNT(*) FROM {table_name} WHERE Toán >= 1 AND Toán < 5 AND Toán <> -1",
    "Toán KTG": f"SELECT COUNT(*) FROM {table_name} WHERE Toán = -1",
}
results1 = {}

sql_queries2 = {
    "[Ngữ Văn]giỏi": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngữ Văn] >= 8 AND [Ngữ Văn] <> -1",
    "[Ngữ Văn]TB": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngữ Văn] >= 5 AND [Ngữ Văn] < 8 AND [Ngữ Văn] <> -1",
    "[Ngữ Văn]yếu": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngữ Văn] >= 1 AND [Ngữ Văn] < 5 AND [Ngữ Văn] <> -1",
    "[Ngữ Văn]KTG": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngữ Văn] = -1",
}
results2 = {}

sql_queries3 = {
    "[Ngoại Ngữ]giỏi": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngoại Ngữ] >= 8 AND [Ngoại Ngữ] <> -1",
    "[Ngoại Ngữ]TB": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngoại Ngữ] >= 5 AND [Ngoại Ngữ] < 8 AND [Ngoại Ngữ] <> -1",
    "[Ngoại Ngữ]yếu": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngoại Ngữ] >= 1 AND [Ngoại Ngữ] < 5 AND [Ngoại Ngữ] <> -1",
    "[Ngoại Ngữ]KTG": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngoại Ngữ] = -1",
}
results3 = {}

sql_queries4 = {
    "[KHTN]giỏi": f"""
        SELECT COUNT(*) FROM {table_name} 
        WHERE ([Hóa học] + [Vật Lý] + [Sinh học]) / 3 >= 8 
        AND [Hóa học] <> -1 AND [Vật Lý] <> -1 AND [Sinh học] <> -1
    """,
    "[KHTN]TB": f"""
        SELECT COUNT(*) FROM {table_name} 
        WHERE ([Hóa học] + [Vật Lý] + [Sinh học]) / 3 >= 5 AND ([Hóa học] + [Vật Lý] + [Sinh học]) / 3 < 8
        AND [Hóa học] <> -1 AND [Vật Lý] <> -1 AND [Sinh học] <> -1
    """,
    "[KHTN]yếu": f"""
        SELECT COUNT(*) FROM {table_name} 
        WHERE ([Hóa học] + [Vật Lý] + [Sinh học]) / 3 >= 1 AND ([Hóa học] + [Vật Lý] + [Sinh học]) / 3 < 5
        AND [Hóa học] <> -1 AND [Vật Lý] <> -1 AND [Sinh học] <> -1
    """,
    
    "[KHTN]KTG": f"""
        SELECT COUNT(*) FROM {table_name} 
        WHERE [Hóa học] = -1 OR [Vật Lý] = -1 OR [Sinh học] = -1
    """,
}
results4 = {}

sql_queries5 = {
    "[KHXH]giỏi": f"""
        SELECT COUNT(*) FROM {table_name} 
        WHERE ([Lịch Sử] + [Địa Lý] + [Giáo dục công dân]) / 3 >= 8
        AND [Lịch Sử] <> -1 AND [Địa Lý] <> -1 AND [Giáo dục công dân] <> -1
    """,
    "[KHXH]TB": f"""
        SELECT COUNT(*) FROM {table_name} 
        WHERE ([Lịch Sử] + [Địa Lý] + [Giáo dục công dân]) / 3 >= 5 AND ([Lịch Sử] + [Địa Lý] + [Giáo dục công dân]) / 3 < 8
        AND [Lịch Sử] <> -1 AND [Địa Lý] <> -1 AND [Giáo dục công dân] <> -1
    """,
    "[KHXH]yếu": f"""
        SELECT COUNT(*) FROM {table_name} 
        WHERE ([Lịch Sử] + [Địa Lý] + [Giáo dục công dân]) / 3 >= 1 AND ([Lịch Sử] + [Địa Lý] + [Giáo dục công dân]) / 3 < 5
        AND [Lịch Sử] <> -1 AND [Địa Lý] <> -1 AND [Giáo dục công dân] <> -1
    """,
    "[KHXH]KTG": f"""
        SELECT COUNT(*) FROM {table_name} 
        WHERE [Lịch Sử] = -1 OR [Địa Lý] = -1 OR [Giáo dục công dân] = -1
    """,
}
results5 = {}

with engine.connect() as connection:
    for subject, sql_query in sql_queries1.items():
        result = connection.execute(sa.text(sql_query)).fetchone()
        count = result[0]
        results1[subject] = count
        print(f"Số thí sinh thi môn {subject}: {count}")
    
    for subject, sql_query in sql_queries2.items():
        result = connection.execute(sa.text(sql_query)).fetchone()
        count = result[0]
        results2[subject] = count
        print(f"Số thí sinh thi môn {subject}: {count}")
    
    for subject, sql_query in sql_queries3.items():
        result = connection.execute(sa.text(sql_query)).fetchone()
        count = result[0]
        results3[subject] = count
        print(f"Số thí sinh thi môn {subject}: {count}")
    
    for subject, sql_query in sql_queries4.items():
        result = connection.execute(sa.text(sql_query)).fetchone()
        count = result[0]
        results4[subject] = count
        print(f"Số thí sinh thi môn {subject}: {count}")
    
    for subject, sql_query in sql_queries5.items():
        result = connection.execute(sa.text(sql_query)).fetchone()
        count = result[0]
        results5[subject] = count
        print(f"Số thí sinh thi môn {subject}: {count}")

# Dữ liệu cho các biểu đồ tròn
labels = ['không tham gia thi', 'Trung bình', 'Khá', 'Giỏi']

sizes1 = [results1['Toán KTG'], results1['Toán yếu'], results1['Toán TB'], results1['Toán giỏi']]
sizes2 = [results2['[Ngữ Văn]KTG'], results2['[Ngữ Văn]yếu'], results2['[Ngữ Văn]TB'], results2['[Ngữ Văn]giỏi']]
sizes3 = [results3['[Ngoại Ngữ]KTG'],  results3['[Ngoại Ngữ]yếu'], results3['[Ngoại Ngữ]TB'], results3['[Ngoại Ngữ]giỏi']]
sizes4 = [results4['[KHTN]KTG'], results4['[KHTN]yếu'], results4['[KHTN]TB'], results4['[KHTN]giỏi']]
sizes5 = [results5['[KHXH]KTG'], results5['[KHXH]yếu'], results5['[KHXH]TB'], results5['[KHXH]giỏi']]

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', "green"]
explode = (0, 0, 0, 0)  # làm nổi bật 1 phần 

# Tạo một figure với 5 subplot
fig, axs = plt.subplots(2, 3, figsize=(18, 12))


def plot_donut(ax, sizes, title):
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, 
                                      autopct='%1.1f%%', startangle=140, pctdistance=0.85)
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    ax.axis('equal')  # Đảm bảo biểu đồ tròn
    ax.set_title(title)

# Biểu đồ tròn đầu tiên
plot_donut(axs[0, 0], sizes1, 'Biểu đồ phổ điểm Toán')

# Biểu đồ tròn thứ hai
plot_donut(axs[0, 1], sizes2, 'Biểu đồ phổ điểm Ngữ Văn')

# Biểu đồ tròn thứ ba
plot_donut(axs[0, 2], sizes3, 'Biểu đồ phổ điểm Ngoại Ngữ')

# Biểu đồ tròn thứ tư
plot_donut(axs[1, 0], sizes4, 'Biểu đồ phổ điểm KHTN')

# Biểu đồ tròn thứ năm
plot_donut(axs[1, 1], sizes5, 'Biểu đồ phổ điểm KHXH')

# Ẩn trục không sử dụng
axs[1, 2].axis('off')

# Tạo chú thích thành phần ở góc dưới bên phải
fig.legend(labels, loc='right', frameon=False)

# Lưu biểu đồ vào file ảnh
plt.savefig('multi_pie_charts.png')

# Hiển thị biểu đồ
plt.show()
