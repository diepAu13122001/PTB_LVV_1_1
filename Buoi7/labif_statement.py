# Viết chương trình nhập vào một số,
# xuất ra màn hình kết quả khi chia lấy phần nguyên của số đó và 7:
# num = input("Nhap vao 1 so: ")
# result = int(num) // 7
# print(type(result)) # kieu du lieu tuy thuoc vao so chia (num)
# print("Chia lay phan nguyen cho 7: " + str(result))

# Viết chương trình nhập vào một chuỗi, 
# kiểm tra nếu chuỗi đó là "Hello" thì in ra màn hình "Hi bro", 
# ngược lại in ra "Who are you?": 
# # Buoc1: luu tru gia tri nguoi dung nhap vao
# user_input = input("Nhap 1 chuoi: ")
# # Buoc2: kiem tra gia tri
# if (user_input == "Hello"):
#     print("Hi bro")
# else:
#     print("Who are you?")

# Viết chương trình nhập vào một số, 
# in ra màn hình phần dư của số đó khi chia cho 2: 
# num = float(input("Nhap mot so: "))
# # chen bien vao string bang f va dau {}
# print(f"Chia phan du voi 2: {num%2}")

# Viết chương trình nhập vào tuổi, 
# in ra màn hình tuổi của người đó 10 năm sau:
# age = int(input("Nhap vao 1 tuoi: "))
# sum = age + 10
# print("Muoi nam nua la:" + str(sum))

# Viết chương trình nhập vào điểm, kiểm tra và in ra xếp loại, nếu:
# + điểm < 0 hoặc điểm > 10: không hợp lệ
# + điểm < 4: yếu
# + điểm < 6: trung bình
# + điểm < 8: khá
# + điểm < 9.5: tốt
# + còn lại: xuất sắc.

# Buoc1: nhap diem
diem = float(input("Nhap diem: "))
# Buoc2: kiem tra diem
if (diem < 0 or diem > 10):
    print("Khong hop le")
elif diem < 4:
    print("Yeu")
elif diem < 6:
    print("Trung binh")
elif diem < 8:
    print("Kha")
elif diem < 9.5:
    print("Tot")
else:
    print("Xuat sac")
