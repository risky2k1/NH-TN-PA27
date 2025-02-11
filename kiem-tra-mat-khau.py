# Take password from user and calculate the security score:
# If password length is greater than 8 and password includes normal characters	🡪     +10
# If password includes upper characters	🡪     +10
# If password includes number		🡪     +20
# If password includes special characters	🡪     +30
# If password includes all above	🡪     +30


# day_so = [1, 4, 7, 8, 4, 23, 6, 8, 9]
# Từ mảng day_so chuyển về mảng chỉ toàn true hoặc false(tự đặt điều kiện)

# Kiểm tra tất cả cả số trong list có >0 hay không
# result = [True, True, True, True, True, True, True, True, True, True]
# Kiểm tra tất cả cả số trong list có >5 hay không
# result2 = [False, False, True, False, True, True, True, True, True, True]

# Sử dụng list comprehension
# Kiểm tra từng số có > 0 hoặc lớn hơn 5 hay không
# result = [i > 0 for i in day_so]
# result2 = [i > 5 for i in day_so]
# In ra các số lớn 5
# result3 = [f'Số lớn hơn 5 là: {i}' for i in day_so if i > 5]

# print(result)
# print(result2)

# Kiểm tra 7 có nằm trong day_so hay không?

#   any()
import string

INPUT_PASSWORD = input('Nhập vào mật khẩu cần kiểm tra: ')

# Kiểm tra xem có kí tự thường ở trong mật khẩu hay không:
ket_qua_kiem_tra_ki_tu_thuong = [char.islower() for char in INPUT_PASSWORD]
ket_qua_kiem_tra_ki_tu_hoa = [char.isupper() for char in INPUT_PASSWORD]
ket_qua_kiem_tra_ki_tu_so = [char.isdigit() for char in INPUT_PASSWORD]
ket_qua_kiem_tra_ki_tu_dac_biet = [char in string.punctuation for char in INPUT_PASSWORD]

SCORE = 0
if len(INPUT_PASSWORD) >= 8 and any(ket_qua_kiem_tra_ki_tu_thuong):
    SCORE += 10
if any(ket_qua_kiem_tra_ki_tu_hoa):
    SCORE += 10
if any(ket_qua_kiem_tra_ki_tu_so):
    SCORE += 20
if any(ket_qua_kiem_tra_ki_tu_dac_biet):
    SCORE += 30
# Nếu toàn bộ 4 điều kiện trên đúng thì +30
if (len(INPUT_PASSWORD) >= 8 and any(ket_qua_kiem_tra_ki_tu_thuong) and any(ket_qua_kiem_tra_ki_tu_hoa)
        and any(ket_qua_kiem_tra_ki_tu_so) and any(ket_qua_kiem_tra_ki_tu_dac_biet)):
    SCORE += 30

    # Về nhà :  <30 điểm in ra 'Mật khẩu yếu
    # 30 - 70 In ra Mật khẩu vừa
    # trên 70 In ra Mật khẩu mạnh
print(SCORE)
