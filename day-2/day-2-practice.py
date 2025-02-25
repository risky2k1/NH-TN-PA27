# Yêu cầu:
# Tạo ra 1 class Student: có các thuộc tính
# - Điểm chuyên cần
# - Tên
# - Lớp
# - Trường
# - Điểm toán
# - Điểm văn
# - Điểm anh

class Student:
    def __init__(self, ten, lop, truong):
        self.ten = ten
        self.truong = truong
        self.lop = lop

    def them_diem(self, diem_toan, diem_van, diem_anh):
        self.toan = diem_toan
        self.van = diem_van
        self.anh = diem_anh

    def tinh_diem_trung_binh(self):
        diem_trung_binh = (self.toan + self.van + self.anh) / 3
        return diem_trung_binh

    def them_diem_chuyen_can(self, diem_chuyen_can):
        self.diem_chuyen_can = diem_chuyen_can

    def duoc_len_lop(self):
        # điểm trung bình 3 môn >= 6.5
        # điểm chuyên cân >= 70% (70/100, 7/10)
        diem_trung_binh_cua_hoc_sinh = self.tinh_diem_trung_binh()
        if diem_trung_binh_cua_hoc_sinh >= 6.5 and self.diem_chuyen_can > 7:
            print('Đủ điều kiện lên lớp')
        else:
            print('Không đủ điều kiện')


student_1 = Student('Pham Minh Tuan', '12A3', 'THPT Xuan Truong B')
student_1.them_diem(10, 9, 8)
student_1.them_diem_chuyen_can(8)
print(student_1.tinh_diem_trung_binh())
student_1.duoc_len_lop()

student_2 = Student('Pham Van A', '12A1', 'THPT Xuan Truong A')
student_2.them_diem(9, 8, 7)
student_2.them_diem_chuyen_can(8)
print(student_2.tinh_diem_trung_binh())
student_2.duoc_len_lop()

student_3 = Student('NGuyen Van B', '12A2', 'THPT Xuan Truong C')
student_3.them_diem(8, 7, 6)
student_3.them_diem_chuyen_can(5)
print(student_3.tinh_diem_trung_binh())
student_3.duoc_len_lop()
