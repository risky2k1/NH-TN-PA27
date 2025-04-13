# Cách 1: open()
# file = open('name.txt')
# Đọc nội dung file:
# content = file.readlines()

# D:\python\NH-TN-PA27\day-5\name.txt
# D:\python\NH-TN-PA27\day-5> 
# print(content)
# file.close()

# Cách 2:
with open('name.txt','r') as danh_sach_hoc_vien:
    # Đọc 1 dòng
    # single_line = danh_sach_hoc_vien.readline()
    # Đọc tất các dòng
    cac_hoc_vien = danh_sach_hoc_vien.readlines()
    # print(single_line)
    print(cac_hoc_vien)

