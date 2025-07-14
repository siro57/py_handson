a = int(input("数字を入力してください:"))

for i in range(2, limit+1):
    for j in range a // i == 0 :
        print(False)
    else:
        print(True)     

x = 0
limit = 20000

for i in range(2, limit + 1):
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            break
    else:
        x += i
print(x)