# Pyramid Program using numbers

num = int(input("Enter a number :"))

for i in range(1,num+1):
    print(' '*(num-i), end='')

    for j in range(1,i+1):
        print(j, end=' ')
    print()

# Enter a number :10
#          1
#         1 2
#        1 2 3
#       1 2 3 4
#      1 2 3 4 5
#     1 2 3 4 5 6
#    1 2 3 4 5 6 7
#   1 2 3 4 5 6 7 8
#  1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10