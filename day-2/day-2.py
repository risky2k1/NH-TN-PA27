class Robot:
    # - Đặc điểm , tính chất của 1 người (Attribute)
    # - Hành động (Methods)
    # Xây dựng lên cái bản thiết kế hay là mô hình về 1 người

    # sử dụng hàm khởi tạo để thông báo và gán các attribute cho class đó
    # Nếu dùng hàm khởi tạo thì khi tajo ra các Object thì phải khai báo bằng đó thuộc tính
    def __init__(self, skin_color, name, age, hair_color, height, weight):
        self.skin_color = skin_color
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.height = height
        self.weight = weight


robot_1 = Robot('vang', 'robot-1', '2025', 'mau den', '170', 70)


class Robot2:
    def __init__(self, ten, nam_san_xuat):
        self.ten = ten
        self.nam_san_xuat = nam_san_xuat

    def run(self):
        print(f" {self.ten} đang chạy")

    def jump(self):
        print(f'{self.ten} đang nhảy')


robot_2 = Robot2('Robot 2', 2025)
robot_2.mau_sac = 'vang'
robot_2.chieu_cao = 180
robot_2.can_nang = 70

print(robot_2.mau_sac)
print(robot_2.chieu_cao)
print(robot_2.can_nang)
print(robot_2.run())