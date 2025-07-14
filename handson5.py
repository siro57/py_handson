a = int(input("数字を入力してください:"))
b = int(input("数字を入力してください:"))

if 1 < a and 1 < b:
    for i in range(2, a+1):
        for j in range(2, (i//2)+1):
            if i % j == 0:
                print("false")
            else:
                print("aは素数")    
                for i in range(2,b+1):
                    for j in range (2, (i//2)+1):
                        if i % j == 0:
                            print("false")
                        else:
                            print("True")     
else:
    print("素数ではない")