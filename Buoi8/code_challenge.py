# Tinh tong so chan tu so nguyen a => b -------------------------
# # nhap 2 so nguyen a, b
# a = int(input("Nhap so nguyen a: "))
# b = int(input("Nhap so nguyen b: "))
# sum = 0
# # kiem tra a co chan khong?
# if a % 2 == 0:
#     # a la so chan
#     for i in range(a, b, 2):
#         # tinh tong bang cach cong don
#         # sum = sum + i
#         sum += i
# else:
#     # a la so le
#     for i in range(a + 1, b, 2):
#         sum += i

# #  in ket qua 
# print(f"Tong so chan trong (a, b): {sum}")

# in bang cuu chuong (2) --------------------------------------
for i in range(2, 11):
    # nhan so
    result = 2 * i
    #  doi i tu int => str 
    print("2 x " + str(i) + " = " + str(result))
