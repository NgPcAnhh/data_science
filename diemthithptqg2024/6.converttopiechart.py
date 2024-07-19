import matplotlib.pyplot as plt
import sqlalchemy as sa

# Khai báo thông tin kết nối database
engine = sa.create_engine(
    "mssql+pyodbc://sa:123456789@DESKTOP-L9G0DQ6/phantichdiemthi?driver=ODBC+Driver+17+for+SQL+Server"
)

# Xác định tên bảng
table_name = "ketquathithptqg"

# Định nghĩa truy vấn SQL
sql_query = """
    SELECT 
    SUM(CASE WHEN num_negative_ones = 3 THEN 1 ELSE 0 END) AS mon3,
    SUM(CASE WHEN num_negative_ones = 4 THEN 1 ELSE 0 END) AS mon4,
    SUM(CASE WHEN num_negative_ones = 5 THEN 1 ELSE 0 END) AS mon5,
    SUM(CASE WHEN num_negative_ones = 6 THEN 1 ELSE 0 END) AS mon6
    FROM (
    SELECT 
        (CASE WHEN Toán = -1 THEN 1 ELSE 0 END +
        CASE WHEN [Ngữ văn] = -1 THEN 1 ELSE 0 END +
        CASE WHEN [Ngoại ngữ] = -1 THEN 1 ELSE 0 END +
        CASE WHEN [Hóa học] = -1 THEN 1 ELSE 0 END +
        CASE WHEN [Vật lý] = -1 THEN 1 ELSE 0 END +
        CASE WHEN [Sinh học] = -1 THEN 1 ELSE 0 END +
        CASE WHEN [Lịch sử] = -1 THEN 1 ELSE 0 END +
        CASE WHEN [Địa lý] = -1 THEN 1 ELSE 0 END +
        CASE WHEN [Giáo dục công dân] = -1 THEN 1 ELSE 0 END) AS num_negative_ones
    FROM ketquathithptqg
    ) subquery
"""

# Thực hiện truy vấn
with engine.connect() as connection:
    result = connection.execute(sa.text(sql_query)).fetchone()
    
# Gán giá trị đếm cho biến
y2, y3, y4, y5 = result

# Tạo biểu đồ 
labels = ['3 môn', '4 môn', '5 môn', '6 môn']
sizes = [y2, y3, y4, y5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # 0.1 cho phần đầu tiên (3 môn), 0 cho các phần còn lại

# Vẽ biểu đồ tròn
plt.figure(figsize=(10, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True)

# Thêm tiêu đề
plt.title('Tỷ lệ thí sinh không thi theo số môn')

plt.legend(labels, title="Số môn không thi", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Hiển thị biểu đồ
plt.axis('equal')  # Đảm bảo biểu đồ tròn
plt.show()