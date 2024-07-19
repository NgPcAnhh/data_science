import requests
from bs4 import BeautifulSoup
# thu thập thông tin tự động từ script của web và tự động hóa quy trình lấy dữ liệu 

# giới hạn mã thí sinh 
start = 3015500 
end = 3016000
output_file = 'HaiPhong' # thay đổi tên file ở đây 

# crawl dữ liệu để lưu vào file text 
with open(f'{output_file}.txt', "w", encoding="utf-8") as file:  # Mở file để ghi
    for i in range(start,end,1): 
        url = f"https://diemthi.vnexpress.net/index/detail/sbd/0{i}/year/2024" #URL của web tra điểm 
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Lấy nội dung của thẻ div có class là "o-detail-thisinh__info"
            info_div = soup.find("div", class_="o-detail-thisinh__info")
            if info_div:
                file.write(" ".join(info_div.stripped_strings)+ "\t")
                print(" ".join(info_div.stripped_strings)+ "\t")

            # Lấy dữ liệu từ bảng có class là "e-table"
            table = soup.find("table", class_="e-table")
            if table:
                rows = table.find_all("tr")
                for row in rows:
                    cells = row.find_all("td")
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    file.write(" ".join(row_data) + "\t" )
                    print(" ".join(row_data))
        else:
            file.write(f"Không thể kết nối đến trang web với số báo danh {i}\n")
            print(f"Không thể kết nối đến trang web với số báo danh {i}\n")