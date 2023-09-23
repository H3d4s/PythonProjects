import requests

url = 'http://httpbin.org/post'

# Sử dụng 'rb' để mở tệp ở chế độ đọc nhị phân (binary)
files = {'file': ('StudentActiveInSemester.csv', open('Python Projects/Python Web/StudentActiveInSemester.csv', 'rb'))}

subFiles = [
    ('copy1', ('StudentActiveInSemester.csv', open('Python Projects/Python Web/StudentActiveInSemester.csv', 'rb'), 'csv')),
    ('copy2', ('StudentActiveInSemester.csv', open('Python Projects/Python Web/StudentActiveInSemester.csv', 'rb'), 'csv'))
]

r = requests.post(url, files=files, data={'key': 'value'})  # Thay 'data' bằng dữ liệu bạn muốn gửi nếu cần

print(r.status_code)
print(r.text)
