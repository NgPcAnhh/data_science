import pandas as pd
from facebook_page_info_scraper import FacebookPageInfoScraper

# Đọc dữ liệu từ file Excel
excel_file = 'data.xlsx'

# Chọn sheet cần đọc từ file Excel
sheet_name = 'ADS'  # Thay  bằng tên sheet hoặc chỉ số sheet bạn muốn đọc
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Đảm bảo rằng cột A chứa mã UID Facebook
uids = df.iloc[:, 0].tolist()

# Khai báo token API Facebook (nếu cần)
# token = 'your_facebook_api_token'
# scraper = FacebookPageInfoScraper(token=token) # Nếu thư viện hỗ trợ truyền token

# Tạo một danh sách để lưu thông tin trang
results = []

for uid in uids:
    page_url = f'https://www.facebook.com/{uid}'

    # Tạo đối tượng scraper
    scraper = FacebookPageInfoScraper(link=page_url)

    # Lấy thông tin trang
    try:
        page_info = scraper.get_page_info()
        
        # Xử lý dữ liệu trang (thay thế thông tin mẫu bằng dữ liệu thực tế từ scraper)
        page_data = {
            'page_name': page_info.get('page_name', ''),
            'location': page_info.get('location', ''),
            'email': page_info.get('email', ''),
            'phone_number': page_info.get('phone_number', ''),
            'social_media_links': page_info.get('social_media_links', ''),
            'page_website': page_info.get('page_website', ''),
            'page_category': page_info.get('page_category', ''),
            'page_likes': page_info.get('page_likes', ''),
            'page_followers': page_info.get('page_followers', ''),
        }
        results.append(page_data)
    except Exception as e:
        print(f'Error fetching data for UID {uid}: {e}')
        # Thêm một bản ghi trống nếu không thể lấy dữ liệu
        results.append({
            'page_name': '',
            'location': '',
            'email': '',
            'phone_number': '',
            'social_media_links': '',
            'page_website': '',
            'page_category': '',
            'page_likes': '',
            'page_followers': '',
        })

# Tạo DataFrame từ danh sách kết quả
results_df = pd.DataFrame(results)

# Xuất dữ liệu ra file Excel
output_file = 'output.xlsx'
results_df.to_excel(output_file, index=False)

print(f'Data has been exported to {output_file}')
