# Xây dựng ứng dụng đăng ký + đăng nhập
# Hiển thị danh sách các tài khoản có trong chương trình
# OOP

from tkinter import Tk, Button, Entry, Listbox, messagebox, Label


def hien_thi_form_dang_nhap(man_hinh):
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

    Button(text='Đăng nhập').pack(pady=20)


if __name__ == "__main__":
    man_hinh = Tk()
    man_hinh.title('Quản lý đăng nhập')
    man_hinh.minsize(200, 300)

    hien_thi_form_dang_nhap(man_hinh)

    man_hinh.mainloop()
