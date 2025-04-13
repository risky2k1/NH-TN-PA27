# Viết 1 fucntion nhận vào tên file và 1 chuỗi bất kỳ
# Trả ra kết quả True (chuỗi có tồn tại trong File)
# False (Chuỗi không tồn tại trong file đó)

# def is_exists_in_file():
def kiem_tra_chuoi_ton_tai(ten_file, chuoi_can_kiem_tra):
    with open(ten_file, 'r') as file:
        noi_dung_file = file.read()
        ket_qua = chuoi_can_kiem_tra in noi_dung_file
        print(ket_qua)


# Có một mẫu file sẵn có chứa [name]
# Có 1 danh sách các tên:
names = ['Pham Tuan', 'Gia Phuc', 'Gia Hung', 'Anh Minh']
# Thay [name] bằng tên của từng người trong names, và với mỗi người sẽ tạo
# ra 1 file riêng


def generate_welcome_files(template_file, name_list):
    with open(template_file, 'r') as file:
        file_content = file.read()

        for name in name_list:
            if '[name]' in file_content:
                new_content = file_content.replace("[name]", name)
                new_file_name = 'welcome_'+name+'.txt'

                with open(new_file_name, 'w') as new_file:
                    new_file.write(new_content)


generate_welcome_files('welcome.txt', names)
# kiem_tra_chuoi_ton_tai('day-6.txt', 'abc')
