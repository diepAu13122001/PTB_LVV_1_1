n = int(input("Nhap 1 so nguyen: "))
while n == -1:
    n = int(input("Nhap 1 so nguyen: "))

# cach 1: vong for
# for i in range(n, 101):
#     print(i)

# cach 2: vong while
while n < 101:
    print(n)
    n = n + 1