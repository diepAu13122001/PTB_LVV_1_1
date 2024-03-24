# RANGE --------------------------------------------
#  range(<stop>): 0 => stop - 1
#  in "happy new year" 10 lan
# for i in range(10):
#     print("Happy new year", end=" ")
#     print(i)

#  range(<start>, <stop> ): start => stop - 1
# in so tu 10 den 14
# for i in range(10, 15): 
#     print(i) 

# range(<start>, <stop>, <step>): start => stop - 1
# moi so cach step don vi
# dem so nguoc tu 20 den 10, moi so cach nhau 2 don vi
for i in range(20, 10, -2):
    print(i) #20,18,16,14,12

# diem so tu 1 den 10, moi so cach nhau 3 don vi
for i in range(1, 10, 3):
    print(i) #1,4,7