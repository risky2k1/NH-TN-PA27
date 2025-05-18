# Xây dựng ứng dụng đăng ký + đăng nhập
# Hiển thị danh sách các tài khoản có trong chương trình
# OOP

from tkinter import Tk, Button, Entry, Listbox, messagebox, Label


def hien_thi_form_dang_nhap():
    # Xóa các widget đang hiển thị nếu có
    for widget in man_hinh.winfo_children():
        widget.destroy()

    # Xây dựng layout:
    Label(text='ĐĂNG NHẬP', font=('Arial', 20)).pack()
    Label(text='Tài khoản').pack(pady=20)
    tai_khoan = Entry()
    tai_khoan.pack()

    Label(text='Mật khẩu').pack(pady=20)
    mat_khau = Entry()
    mat_khau.pack()

    def xu_ly_dang_nhap():
        tai_khoan_nguoi_dung_nhap = tai_khoan.get()
        mat_khau_nguoi_dung_nhap = mat_khau.get()

        if not tai_khoan_nguoi_dung_nhap or not mat_khau_nguoi_dung_nhap:
            messagebox.showwarning(
                'Cảnh báo', 'Không được để trống tài khoản hoặc mật khẩu')

        with open('tai_khoan.txt', 'r') as file_tai_khoan:
            # Lấy ra các tài khoản từ file
            cac_tai_khoan = file_tai_khoan.readlines()
            # Bỏ đi '\n'
            danh_sach_tai_khoan_moi = [tai_khoan.strip()
                                       for tai_khoan in cac_tai_khoan]

            # Ghép chuỗi tài khoản người dufng nhập tuan-123456
            thong_tin_nguoi_dung_nhap = tai_khoan_nguoi_dung_nhap + \
                '-' + mat_khau_nguoi_dung_nhap

            is_exist = False

            for moi_tai_khoan in danh_sach_tai_khoan_moi:
                if thong_tin_nguoi_dung_nhap == moi_tai_khoan:
                    is_exist = True

            if is_exist:
                messagebox.showinfo('Thành công', 'Đăng nhập thành công')
            else:
                messagebox.showerror(
                    'Có lỗi xảy ra', ' Vui lòng kiểm tra lại tài khoản hoặc mật khẩu')

    Button(text='Đăng nhập', command=xu_ly_dang_nhap).pack(pady=20)

    Button(text='Đăng ký', command=hien_thi_form_dang_ky).pack(pady=20)


def hien_thi_form_dang_ky():
    for widget in man_hinh.winfo_children():
        widget.destroy()
    Label(text='ĐĂNG KÝ', font=('Arial', 20)).pack()

    Label(text='Tài khoản').pack(pady=20)
    tai_khoan_dang_ky = Entry()
    tai_khoan_dang_ky.pack()

    Label(text='Mật khẩu').pack(pady=20)
    mat_khau_dang_ky = Entry()
    mat_khau_dang_ky.pack()

    Label(text='Xác nhận Mật khẩu').pack(pady=20)
    mat_khau_xac_nhan_dang_ky = Entry()
    mat_khau_xac_nhan_dang_ky.pack()

    def xu_ly_dang_ky():
        tk = tai_khoan_dang_ky.get()
        mk = mat_khau_dang_ky.get()
        mkxn = mat_khau_xac_nhan_dang_ky.get()

    Button(text='Đăng ký', command=xu_ly_dang_ky).pack(pady=20)


if __name__ == "__main__":
    man_hinh = Tk()
    man_hinh.title('Quản lý đăng nhập')
    man_hinh.minsize(200, 300)

    hien_thi_form_dang_nhap()

    man_hinh.mainloop()
