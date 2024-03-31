# Khai bao danh sach
food = ["bun bo", "com tam", "tra sua", "kem dau"]
# print(food)
# print(type(food))
print(food[3])  # => kem dau
food[1] = "ca chien xu"
print(food)
print(len(food))  # => int: 4

# duyet qua tung phan tu
for item in food:
    print(item)  # in value (gia tri) cua phan tu
for index in range(len(food)):
    print(index)  # in chi so cua tung phan tu

n = 0
while n < len(food):
    print(f"{n}. {food[n]}")
    n += 1

# Them, xoa phan tu --------------------
# them phan tu vao cuoi danh sach
food.append("coca")
print(food) # [..., coca]
print(len(food)) # => 5
# them tai vi tri mong muon 
food.insert(2, "tra sua")
print(food)
# xoa phan tu cuoi cung
food.pop()
print(food)
# xoa phan tu tai vi tri mong muon
food.remove("tra sua")
print(food)
# xoa het phan tu
food.clear()
print(food)