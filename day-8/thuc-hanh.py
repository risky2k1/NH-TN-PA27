from tkinter import Tk, Label, Entry, Button

root = Tk()

Label(master=root, text='ĐĂNG NHẬP', font=('Arial', 40)).grid(
    column=2, row=1, columnspan=2)

Label(master=root, text='Tài khoản').grid(row=2, column=2)
entry_username = Entry(master=root)
entry_username.grid(row=2, column=3)


Label(master=root, text='Mật khẩu').grid(row=3, column=2)
entry_password = Entry(master=root)
entry_password.grid(row=3, column=3)


Button(master=root, text='Đăng nhập').grid(row=4, column=2, columnspan=2)

root.mainloop()
