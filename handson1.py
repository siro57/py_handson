#1 1×1～9×9の九九の段の答えを出力するようなプログラムを作成せよ。
for num in range(1,10):
    for num2 in range(1,10):
        print(num*num2, end=' ')# 1の段が終わったら空白。
    print(f"「{num}」の段です") #1の段の後ろに表示。   

#2 ユーザーから数字を受けとって、受取った数字が3の倍数の時にfoo、それ以外の時はnooと出力するプログラムを作成せよ
num = int(input("数字を入力してください:"))
if num%3 ==0:
    print("foo")
else:
    print("noo")    

#32つの値を入力し、その数の和を返すプログラムを作成せよ
num1 = int(input("数字を入力してください:"))
num2 = int(input("数字を入力してください:"))

total = num1 + num2
print(total)