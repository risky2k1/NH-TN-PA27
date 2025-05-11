from tkinter import Button, Entry, Listbox, messagebox, Label


class QuanLyTaiKhoan:
    # Attributes:
    def __init__(self, mau_nen, cua_so, ten_chuong_trinh, kich_thuoc_toi_thieu):
        self.mau_nen = mau_nen
        self.cua_so = cua_so
        self.ten_chuong_trinh = ten_chuong_trinh
        self.kich_thuoc_toi_thieu = kich_thuoc_toi_thieu

    def run(self):
        self.cua_so.title(self.ten_chuong_trinh)
        self.cua_so.minsize(
            self.kich_thuoc_toi_thieu[0], self.kich_thuoc_toi_thieu[1])
        self.cua_so.configure(bg=self.mau_nen)

        self.hien_thi_form_dang_nhap()

    def hien_thi_form_dang_nhap(self):
        # Xóa các widget đang hiển thị nếu có
        for widget in self.cua_so.winfo_children():
            widget.destroy()

        # Xây dựng layout:
        Label(text='ĐĂNG NHẬP').pack()
        Label(text='Tài khoản').pack(pady=20)
        tai_khoan = Entry()
        tai_khoan.pack()

        Label(text='Mật khẩu').pack(pady=20)
        mat_khau = Entry()
        mat_khau.pack()

        Button(text='Đăng nhập').pack(pady=20)

        
    # Methods:
