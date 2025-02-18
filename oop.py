# OOP

# Mô hình hóa các đối tượng ở ngoài thành các đối tượng
# có thể tương tác thông qua code

# Keyword: Class (bản thiết kế) - Object (sản phẩm được tạo ra)

# Class:
# Xe thì có màu sắc, kích cỡ, đời xe, di chuyển, phanh, rẽ trái, rẽ phải

# 1 class sẽ có Attributes (thuộc tính) - Methods(Hành động hay hoạt động)

class Car:
    # khai báo methods __init__ (mehtod để khởi tạo 1 class)
    # self = chính cái class đó
    def __init__(self, color, size, model):
        # gán các thuộc tính cho class
        self.color = color
        self.size = size
        self.model = model
    
    # tạo ra các methods cho class:
    def move(self):
        print('Xe đang chạy')

    def brake(self):
        print('Xe phanh lại')

    def turnLeft(self):
        print('Xe rẽ trái')
        
    def turnRight(self):
        print('Xe rẽ phải')

tesla = Car('white','medium','tesla-model-3')

# Truy cập các thuộc tính(attributes)
# print(tesla.color)
# print(tesla.size)
# print(tesla.model)
# Truy cập các phương thức(methods)
# print(tesla.turnRight())
# print(tesla.brake())

xe_ban_tai = Car('yellow','big','ford-ranger')

# print(xe_ban_tai.model)
# print(xe_ban_tai.move())

from mua_quat import dancing_fan

class KhaBanh:
    def __init__(self, ten, tuoi, ngoai_hinh, mau_da, vi_tri_hien_tai):
        self.ten=ten
        self.tuoi=tuoi
        self.ngoai_hinh=ngoai_hinh
        self.mau_da=mau_da
        self.vi_tri_hien_tai=vi_tri_hien_tai

    def muaQuat(self):
        dancing_fan()

    def live_stream(self):
        print('Anh: ' + self.ten + ' đang livestream')

    def phat_ngon(self):
        print('Anh ' + self.ten + ' nói "Ảo thật đấy"')

nbk = KhaBanh('Ngo Ba Kha', 31, 'gầy- xăm trổ', 'vàng', 'trong tù')

print(nbk.ten)
print(nbk.vi_tri_hien_tai)

print(nbk.phat_ngon())
print(nbk.muaQuat())
print(nbk.live_stream())
        
