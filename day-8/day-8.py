# import tkinter
from tkinter import Tk, Label, Button, Entry, messagebox, Listbox

# Tạo màn hình làm việc
man_hinh = Tk()
man_hinh.minsize(400, 200)
# Các widgets:
# - Label - dùng để tạo 1 đoạn text
label_1 = Label(master=man_hinh, text='Welcome to Tkinter')
label_2 = Label(master=man_hinh, text='Hello from Tkinter')
label_3 = Label(master=man_hinh, text='Label số 3')
label_4 = Label(master=man_hinh, text='Label số 4')
label_5 = Label(master=man_hinh, text='Label số 5')

# label_2.pack()
# label_1.pack()

label_1.grid(row=1, column=1)
label_2.grid(row=2, column=1)
label_3.grid(row=3, column=2)
label_4.grid(row=4, column=3)

label_5.place(x=400, y=100)

# Button - Tạo ra các nút
button_1 = Button(master=man_hinh, text='Nút số 1')
button_1.grid(row=1, column=3)
button_2 = Button(master=man_hinh, text='Nút số 2')
button_2.grid(row=1, column=4)

# Entry - Tạo ra các ô nhập liệu  
entry_1 = Entry(master=man_hinh)
entry_1.grid(row=4, column=1)

# Listbox - Tạo ra 1 vùng hiển thị dữ liệu
listbox_1 = Listbox(master=man_hinh)
listbox_1.grid(row=5, column=2)


# Layouts:
# 3 loại layout:
# Pack - Xếp các Widget theo chiều từ trên xuống dưới
# Grid - Xếp các widget theo dạng lưới
# Place - Đặt các widget vào tọa độ chỉ định

# Pack và Grid không được sử dụng trong cùng 1 màn hình


# BẮt đầu vòng lặp của màn hình
man_hinh.mainloop()
