import pandas as pd
import re
from openpyxl import Workbook

filename = 'DaNang' # thay đổi tên file ở đây

# Đọc nội dung từ file
with open(f'data_thô/{filename}.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Hàm để trích xuất thông tin từ chuỗi dữ liệu
def extract_info(data):
    sbd = re.search(r'Số báo danh: (\d+)', data)
    cum_thi = re.search(r'Cụm thi: (.+?)\s{2,}', data)
    
    subjects = {
        'Toán': '-', 'Ngữ văn': '-', 'Ngoại ngữ': '-',
        'Hóa học': '-', 'Vật lý': '-', 'Sinh học': '-',
        'Lịch sử': '-', 'Địa lý': '-', 'Giáo dục công dân': '-'
    }
    
    for subject, score in re.findall(r'(\w+(?:\s\w+)*)\s([\d.]+)', data):
        if subject in subjects:
            subjects[subject] = score
    
    return {
        'Số báo danh': sbd.group(1) if sbd else '-',
        'Cụm thi': cum_thi.group(1) if cum_thi else '-',
        **subjects
    }

# Tạo workbook và sheet
wb = Workbook()
ws = wb.active

# Đặt tên cho các cột
columns = ['Số báo danh', 'Cụm thi', 'Toán', 'Ngữ văn', 'Ngoại ngữ', 'Hóa học', 'Vật lý', 'Sinh học', 'Lịch sử', 'Địa lý', 'Giáo dục công dân']
ws.append(columns)

# Xử lý từng dòng dữ liệu
for line in data.strip().split('\n\n'):
    info = extract_info(line.strip())
    row = [
        info['Số báo danh'],
        info['Cụm thi'],
        info['Toán'],
        info['Ngữ văn'],
        info['Ngoại ngữ'],
        info['Hóa học'],
        info['Vật lý'],
        info['Sinh học'],
        info['Lịch sử'],
        info['Địa lý'],
        info['Giáo dục công dân']
    ]
    ws.append(row)

# Lưu file Excel
wb.save(f'ketqua_{filename}.xlsx')
print("File Excel đã được tạo: ket_qua_thi.xlsx")

# In ra dữ liệu để kiểm tra
for row in ws.iter_rows(values_only=True):
    print(row)
