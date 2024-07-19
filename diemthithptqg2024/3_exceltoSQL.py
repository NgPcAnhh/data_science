import pandas as pd
from sqlalchemy import create_engine, Table, Column, String, Float, MetaData
import urllib
import os

# Đường dẫn đến file Excel cụ thể
excel_file_path = r'ketqua_TPHCM.xlsx'

# Thông tin kết nối SQL Server
server = 'DESKTOP-L9G0DQ6'
database = 'phantichdiemthi'
username = 'sa'
password = '123456789'
driver = 'ODBC Driver 17 for SQL Server'

# Tạo chuỗi kết nối
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
connection_url = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"

# Tạo engine kết nối
engine = create_engine(connection_url)

# Tạo metadata
metadata = MetaData()

# Định nghĩa bảng
table_name = os.path.splitext(os.path.basename(excel_file_path))[0]
ketqua_table = Table(table_name, metadata,
    Column('Sobaodanh', String(8), primary_key=True),
    Column('CumThi', String(50)),
    Column('Toan', Float),
    Column('Van', Float),
    Column('Ly', Float),
    Column('Hoa', Float),
    Column('Sinh', Float),
    Column('KhoaHocTuNhien', Float),
    Column('Su', Float),
    Column('Dia', Float),
    Column('GDCD', Float),
    Column('KhoaHocXaHoi', Float),
    Column('NgoaiNgu', Float)
)

try:
    # Tạo bảng trong SQL Server
    metadata.create_all(engine)
    print(f"Đã tạo bảng {table_name} trong SQL Server")

    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(excel_file_path)

    # Chèn dữ liệu vào SQL Server
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    
    print(f"Đã import thành công dữ liệu từ {excel_file_path} vào bảng {table_name}")
except Exception as e:
    print(f"Lỗi: {str(e)}")

print("Quá trình tạo bảng và import dữ liệu đã hoàn tất!")