print('''---------------------切片---------------------
''')

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print("L=", L)
print("L[0:3]=", L[0:3])
print("L[1:3]=", L[1:3])
# 记住倒数第一个元素的索引是-1。
print("L[-2:]=", L[-2:])
print("L[-2:-1]=", L[-2:-1])

L1 = list(range(100))
print("\nL1=", L1)
print("L1[:10]=", L1[:10])  # 前10个数
print("L1[-10:]=", L1[-10:])  # 后10个数
print("L1[10:20]=", L1[10:20])  # 前11-20个数：
print("L1[:10:2]=", L1[:10:2])  # 前10个数，每两个取一个：
print("L1[::5]=", L1[::5])  # 所有数，每5个取一个：
# print ("L1[:]=", L1[:])  # 只写[:]就可以原样复制一个list

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print("\n(0, 1, 2, 3, 4, 5)[:3]=", (0, 1, 2, 3, 4, 5)[:3])

print("\n'ABCDEFG'[:3]=", 'ABCDEFG'[:3])
print("'ABCDEFG'[::2]=", 'ABCDEFG'[::2])
