import matplotlib.pyplot as plt


import sqlalchemy as sa

# Khai báo thông tin kết nối database
engine = sa.create_engine(
    "mssql+pyodbc://sa:123456789@DESKTOP-L9G0DQ6/phantichdiemthi?driver=ODBC+Driver+17+for+SQL+Server"
)

# Xác định tên bảng
table_name = "ketquathithptqg"

# Định nghĩa truy vấn SQL cho từng môn thi
sql_queries = {
    "Toán": f"SELECT COUNT(*) FROM {table_name} WHERE Toán <> -1",
    "Văn": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngữ Văn] <> -1",
    "Ngoại ngữ": f"SELECT COUNT(*) FROM {table_name} WHERE [Ngoại ngữ] <> -1",
    "Hóa học": f"SELECT COUNT(*) FROM {table_name} WHERE [Hóa học] <> -1",
    "Vật lý": f"SELECT COUNT(*) FROM {table_name} WHERE [Vật lý] <> -1",
    "Sinh học": f"SELECT COUNT(*) FROM {table_name} WHERE [Sinh học] <> -1",
    "Lịch sử": f"SELECT COUNT(*) FROM {table_name} WHERE [Lịch sử] <> -1",
    "Địa lý": f"SELECT COUNT(*) FROM {table_name} WHERE [Địa Lý] <> -1",
    "GDCD": f"SELECT COUNT(*) FROM {table_name} WHERE [Giáo Dục Công Dân] <> -1",
}

# Khởi tạo dictionary để lưu kết quả
results = {}

# Lặp qua từng môn thi và thực hiện truy vấn
with engine.connect() as connection:
    for subject, sql_query in sql_queries.items():
        result = connection.execute(sa.text(sql_query)).fetchone()
        count = result[0]
        results[subject] = count
        print(f"Số thí sinh thi môn {subject}: {count}")

# Gán giá trị đếm cho biến
y1 = results["Toán"]
y2 = results["Văn"]
y3 = results["Ngoại ngữ"]
y4 = results["Hóa học"]
y5 = results["Vật lý"]
y6 = results["Sinh học"]
y7 = results["Lịch sử"]
y8 = results["Địa lý"]
y9 = results["GDCD"]


# tạo biểu đồ 
x = ['Toán', "Ngữ Văn", 'Ngoại Ngữ', 'Hóa học', "Vật Lý", "Sinh học", 'Lịch sử', "Địa lý", "GDCD"]
y = [y1,y2,y3,y4,y5,y6,y7,y8,y9]

plt.figure(figsize=(12, 8))
bars = plt.bar(x, y)

# Thêm tiêu đề và nhãn
plt.title('Biểu đồ số lượng thí sinh đăng kí các môn thi')
plt.xlabel('Các môn đăng kí')
plt.ylabel('Số lượng thi sinh đã dự thi')

# Thêm số lên trên các cột
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), ha='center', va='bottom')  # `ha` là viết tắt của `horizontal alignment`

# Hiển thị biểu đồ
plt.show()