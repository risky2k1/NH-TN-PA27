# Các mode: r - Read(Chỉ đọc),  w - Write (Ghi đè), a - append (Thêm vào)

# R:
# with open('day-6.txt', 'r') as file:
    # Đọc nội dung file:
    # file_content = file.read()
    # print(file_content)

    # Đọc dòng
    # 1 dòng:
    # line = file.readline()
    # print(line)
    # Đọc tất cả các dòng
    # -> trả về 1 danh sách các dòng với mỗi dòng 1 phần tử
    # lines = file.readlines()
    # print(lines)

# W:
# with open('day-6.txt', 'w') as file:
    # Ghi vào file nội dung
    # Thay đổi toàn bộ nội dung file
    # file.write('List students')
# Ctrl + /

# A:
with open('day-6.txt', 'a') as file:
    file.write('Student no.5')
